"""
AST Node Transformer for PvZ Fusion Visual Scripting Transpiler.

Converts standard Python constructs (if/elif/else, while, for in range, match/case, print, variable assignments)
into corresponding PvZ Fusion visual scripting DSL context managers and node graph API calls.
"""

from __future__ import annotations

import ast
from typing import Any, List, Optional, Set


class PvZNodeTransformer(ast.NodeTransformer):
    """Transforms high-level Python AST nodes into visual scripting DSL equivalents."""

    def __init__(self, pvn_alias: str = "pvn"):
        super().__init__()
        self.pvn_alias: str = pvn_alias
        self.branch_counter: int = 0
        self.loop_counter: int = 0
        self.switch_counter: int = 0
        self.known_vars: Set[str] = set()

    def _pvn_attr(self, name: str) -> ast.Attribute:
        """Helper to create `pvn.<name>` AST attribute."""
        return ast.Attribute(
            value=ast.Name(id=self.pvn_alias, ctx=ast.Load()),
            attr=name,
            ctx=ast.Load(),
        )

    def _is_var_init(self, value: ast.expr) -> bool:
        """Checks if an expression initializes an IntVar, FloatVar, BoolVar, StrVar, or ListVar."""
        if isinstance(value, ast.Call):
            func = value.func
            if isinstance(func, ast.Name) and func.id in ("IntVar", "FloatVar", "BoolVar", "StrVar", "ListVar"):
                return True
            if isinstance(func, ast.Attribute) and func.attr in ("IntVar", "FloatVar", "BoolVar", "StrVar", "ListVar"):
                return True
        return False

    def visit_Assign(self, node: ast.Assign) -> Any:
        # First visit the value
        node.value = self.visit(node.value)

        # Check if targets are being initialized as visual script variables
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id
                if self._is_var_init(node.value):
                    self.known_vars.add(var_name)
                    return node

                # If this variable is already known as an engine variable, convert `var = val` to `var.set(val)`
                if var_name in self.known_vars:
                    set_call = ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id=var_name, ctx=ast.Load()),
                            attr="set",
                            ctx=ast.Load(),
                        ),
                        args=[node.value],
                        keywords=[],
                    )
                    return ast.copy_location(ast.Expr(value=set_call), node)

        return node

    def visit_Call(self, node: ast.Call) -> Any:
        # Check if calling standard python `print(...)`
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            # Replace with `pvn.Print(*args, **kwargs)`
            node.func = self._pvn_attr("Print")

        self.generic_visit(node)
        return node

    def visit_If(self, node: ast.If) -> Any:
        """Transforms an if/elif/else block into chained `pvn.If(...)` context managers."""
        # Check if there is an else or elif chain
        if not node.orelse:
            # Simple if statement -> with pvn.If(test): body
            transformed_test = self.visit(node.test)
            transformed_body = [self.visit(s) for s in node.body]
            # Flatten any lists returned by visitors inside body
            flat_body = []
            for s in transformed_body:
                if isinstance(s, list):
                    flat_body.extend(s)
                elif s is not None:
                    flat_body.append(s)

            with_stmt = ast.With(
                items=[
                    ast.withitem(
                        context_expr=ast.Call(
                            func=self._pvn_attr("If"),
                            args=[transformed_test],
                            keywords=[],
                        ),
                        optional_vars=None,
                    )
                ],
                body=flat_body,
            )
            return ast.copy_location(with_stmt, node)

        # Chained If / Elif / Else
        branch_name = f"_branch_{self.branch_counter}"
        self.branch_counter += 1

        result_statements: List[ast.stmt] = []

        # 1. Main `If` branch: with pvn.If(test) as _branch:
        transformed_test = self.visit(node.test)
        transformed_body = []
        for s in node.body:
            res = self.visit(s)
            if isinstance(res, list):
                transformed_body.extend(res)
            elif res is not None:
                transformed_body.append(res)

        first_with = ast.With(
            items=[
                ast.withitem(
                    context_expr=ast.Call(
                        func=self._pvn_attr("If"),
                        args=[transformed_test],
                        keywords=[],
                    ),
                    optional_vars=ast.Name(id=branch_name, ctx=ast.Store()),
                )
            ],
            body=transformed_body,
        )
        result_statements.append(ast.copy_location(first_with, node))

        # 2. Process Elif / Else branches in orelse
        curr_orelse = node.orelse
        while curr_orelse:
            if len(curr_orelse) == 1 and isinstance(curr_orelse[0], ast.If):
                # Elif branch: with _branch.Elif(elif_test) as _branch:
                elif_node = curr_orelse[0]
                elif_test = self.visit(elif_node.test)
                elif_body = []
                for s in elif_node.body:
                    res = self.visit(s)
                    if isinstance(res, list):
                        elif_body.extend(res)
                    elif res is not None:
                        elif_body.append(res)

                elif_with = ast.With(
                    items=[
                        ast.withitem(
                            context_expr=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id=branch_name, ctx=ast.Load()),
                                    attr="Elif",
                                    ctx=ast.Load(),
                                ),
                                args=[elif_test],
                                keywords=[],
                            ),
                            optional_vars=ast.Name(id=branch_name, ctx=ast.Store()),
                        )
                    ],
                    body=elif_body,
                )
                result_statements.append(ast.copy_location(elif_with, elif_node))
                curr_orelse = elif_node.orelse
            else:
                # Final Else branch: with _branch.Else:
                else_body = []
                for s in curr_orelse:
                    res = self.visit(s)
                    if isinstance(res, list):
                        else_body.extend(res)
                    elif res is not None:
                        else_body.append(res)

                else_with = ast.With(
                    items=[
                        ast.withitem(
                            context_expr=ast.Attribute(
                                value=ast.Name(id=branch_name, ctx=ast.Load()),
                                attr="Else",
                                ctx=ast.Load(),
                            ),
                            optional_vars=None,
                        )
                    ],
                    body=else_body,
                )
                result_statements.append(else_with)
                break

        return result_statements

    def visit_While(self, node: ast.While) -> Any:
        """Transforms a `while cond:` into `with pvn.While(cond):`."""
        transformed_test = self.visit(node.test)
        transformed_body = []
        for s in node.body:
            res = self.visit(s)
            if isinstance(res, list):
                transformed_body.extend(res)
            elif res is not None:
                transformed_body.append(res)

        with_stmt = ast.With(
            items=[
                ast.withitem(
                    context_expr=ast.Call(
                        func=self._pvn_attr("While"),
                        args=[transformed_test],
                        keywords=[],
                    ),
                    optional_vars=None,
                )
            ],
            body=transformed_body,
        )
        return ast.copy_location(with_stmt, node)

    def visit_For(self, node: ast.For) -> Any:
        """Transforms `for ... in range(...)` or `for p in generator:` into visual script loops."""
        iter_expr = node.iter
        target = node.target

        # Check if iter is `range(...)`
        is_range = False
        if isinstance(iter_expr, ast.Call):
            if (isinstance(iter_expr.func, ast.Name) and iter_expr.func.id == "range") or (
                isinstance(iter_expr.func, ast.Attribute) and iter_expr.func.attr == "range"
            ):
                is_range = True

        if is_range:
            loop_var = f"_loop_{self.loop_counter}"
            self.loop_counter += 1

            args = iter_expr.args
            if len(args) == 1:
                # range(count)
                count_expr = self.visit(args[0])
                index_assign = ast.Assign(
                    targets=[target],
                    value=ast.Attribute(
                        value=ast.Name(id=loop_var, ctx=ast.Load()),
                        attr="index",
                        ctx=ast.Load(),
                    ),
                )
            elif len(args) == 2:
                # range(start, stop) -> count = stop - start, index = start + loop.index
                start_expr = self.visit(args[0])
                stop_expr = self.visit(args[1])
                count_expr = ast.BinOp(left=stop_expr, op=ast.Sub(), right=start_expr)
                index_assign = ast.Assign(
                    targets=[target],
                    value=ast.BinOp(
                        left=start_expr,
                        op=ast.Add(),
                        right=ast.Attribute(
                            value=ast.Name(id=loop_var, ctx=ast.Load()),
                            attr="index",
                            ctx=ast.Load(),
                        ),
                    ),
                )
            elif len(args) == 3:
                # range(start, stop, step)
                start_expr = self.visit(args[0])
                stop_expr = self.visit(args[1])
                step_expr = self.visit(args[2])
                count_expr = ast.BinOp(
                    left=ast.BinOp(left=stop_expr, op=ast.Sub(), right=start_expr),
                    op=ast.FloorDiv(),
                    right=step_expr,
                )
                index_assign = ast.Assign(
                    targets=[target],
                    value=ast.BinOp(
                        left=start_expr,
                        op=ast.Add(),
                        right=ast.BinOp(
                            left=ast.Attribute(
                                value=ast.Name(id=loop_var, ctx=ast.Load()),
                                attr="index",
                                ctx=ast.Load(),
                            ),
                            op=ast.Mult(),
                            right=step_expr,
                        ),
                    ),
                )
            else:
                count_expr = self._pvn_attr("For")

            transformed_body = [index_assign]
            for s in node.body:
                res = self.visit(s)
                if isinstance(res, list):
                    transformed_body.extend(res)
                elif res is not None:
                    transformed_body.append(res)

            with_stmt = ast.With(
                items=[
                    ast.withitem(
                        context_expr=ast.Call(
                            func=self._pvn_attr("For"),
                            args=[count_expr],
                            keywords=[],
                        ),
                        optional_vars=ast.Name(id=loop_var, ctx=ast.Store()),
                    )
                ],
                body=transformed_body,
            )
            return ast.copy_location(with_stmt, node)

        # If not range, check if it's an iterable query (like Lawnf.for_each_plant_on_lawn())
        # Transform `for x in query:` -> `with query as x:`
        transformed_iter = self.visit(node.iter)
        transformed_body = []
        for s in node.body:
            res = self.visit(s)
            if isinstance(res, list):
                transformed_body.extend(res)
            elif res is not None:
                transformed_body.append(res)

        with_stmt = ast.With(
            items=[
                ast.withitem(
                    context_expr=transformed_iter,
                    optional_vars=target,
                )
            ],
            body=transformed_body,
        )
        return ast.copy_location(with_stmt, node)

    def visit_Match(self, node: ast.Match) -> Any:
        """Transforms Python 3.10+ `match / case` statements into `pvn.Switch(...)` blocks."""
        sw_name = f"_sw_{self.switch_counter}"
        self.switch_counter += 1

        transformed_subject = self.visit(node.subject)
        switch_body: List[ast.stmt] = []

        for case in node.cases:
            case_body = []
            for s in case.body:
                res = self.visit(s)
                if isinstance(res, list):
                    case_body.extend(res)
                elif res is not None:
                    case_body.append(res)

            pattern = case.pattern
            # Match wildcard/default: case _:
            if isinstance(pattern, ast.MatchAs) and pattern.name is None:
                case_with = ast.With(
                    items=[
                        ast.withitem(
                            context_expr=ast.Attribute(
                                value=ast.Name(id=sw_name, ctx=ast.Load()),
                                attr="default",
                                ctx=ast.Load(),
                            ),
                            optional_vars=None,
                        )
                    ],
                    body=case_body,
                )
            elif isinstance(pattern, ast.MatchValue):
                # Single value match: case PlantType.SunFlower:
                case_with = ast.With(
                    items=[
                        ast.withitem(
                            context_expr=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id=sw_name, ctx=ast.Load()),
                                    attr="case",
                                    ctx=ast.Load(),
                                ),
                                args=[self.visit(pattern.value)],
                                keywords=[],
                            ),
                            optional_vars=None,
                        )
                    ],
                    body=case_body,
                )
            elif isinstance(pattern, ast.MatchOr):
                # Multi-value OR match: case A | B:
                or_args = [self.visit(p.value) for p in pattern.patterns if isinstance(p, ast.MatchValue)]
                case_with = ast.With(
                    items=[
                        ast.withitem(
                            context_expr=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id=sw_name, ctx=ast.Load()),
                                    attr="case",
                                    ctx=ast.Load(),
                                ),
                                args=or_args,
                                keywords=[],
                            ),
                            optional_vars=None,
                        )
                    ],
                    body=case_body,
                )
            else:
                # Fallback to standard generic case
                case_with = ast.With(
                    items=[
                        ast.withitem(
                            context_expr=ast.Attribute(
                                value=ast.Name(id=sw_name, ctx=ast.Load()),
                                attr="default",
                                ctx=ast.Load(),
                            ),
                            optional_vars=None,
                        )
                    ],
                    body=case_body,
                )

            switch_body.append(case_with)

        outer_with = ast.With(
            items=[
                ast.withitem(
                    context_expr=ast.Call(
                        func=self._pvn_attr("Switch"),
                        args=[transformed_subject],
                        keywords=[],
                    ),
                    optional_vars=ast.Name(id=sw_name, ctx=ast.Store()),
                )
            ],
            body=switch_body,
        )
        return ast.copy_location(outer_with, node)
