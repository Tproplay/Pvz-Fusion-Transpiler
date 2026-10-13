"""
PvZ Fusion AST Transpiler Engine & High-Level Execution Pipeline.

Provides APIs to transpile natural Python level scripts into PvZ Fusion visual scripting
DSL code, compile ASTs to level graph JSON, and decorate level definition functions.
"""

from __future__ import annotations

import ast
import functools
import inspect
import textwrap
from typing import Any, Callable, Dict, Optional, Union

from .transformer import PvZNodeTransformer


def transpile_to_ast(
    source_or_func: Union[str, Callable],
    pvn_alias: str = "pvn",
) -> ast.AST:
    """Parses Python source code or a function, and applies the PvZ AST transformation pass.

    Args:
        source_or_func (str | Callable): Source code string or Python function.
        pvn_alias (str): Name of the imported PvZ Fusion DSL module namespace. Defaults to 'pvn'.

    Returns:
        ast.AST: Transformed Python Abstract Syntax Tree.
    """
    if callable(source_or_func):
        source = textwrap.dedent(inspect.getsource(source_or_func))
    else:
        source = textwrap.dedent(str(source_or_func))

    tree = ast.parse(source)

    # Strip compile_level decorator from the AST if present to avoid recursion
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node.decorator_list = [
                dec for dec in node.decorator_list
                if not (
                    (isinstance(dec, ast.Name) and "compile_level" in dec.id)
                    or (isinstance(dec, ast.Attribute) and dec.attr == "compile_level")
                    or (isinstance(dec, ast.Call) and (
                        (isinstance(dec.func, ast.Name) and "compile_level" in dec.func.id)
                        or (isinstance(dec.func, ast.Attribute) and dec.func.attr == "compile_level")
                    ))
                )
            ]

    transformer = PvZNodeTransformer(pvn_alias=pvn_alias)
    transformed_tree = transformer.visit(tree)
    ast.fix_missing_locations(transformed_tree)
    return transformed_tree


def transpile_source(
    source_or_func: Union[str, Callable],
    pvn_alias: str = "pvn",
) -> str:
    """Transpiles high-level Python code into human-readable PvZ Fusion DSL code.

    Args:
        source_or_func (str | Callable): Source code string or Python function.
        pvn_alias (str): Name of the imported PvZ Fusion DSL module namespace.

    Returns:
        str: Unparsed, formatted DSL Python code.
    """
    tree = transpile_to_ast(source_or_func, pvn_alias=pvn_alias)
    return ast.unparse(tree)


def compile_ast(
    source_or_func: Union[str, Callable],
    globals_dict: Optional[Dict[str, Any]] = None,
    pvn_alias: str = "pvn",
) -> Any:
    """Transpiles and executes Python AST code in the visual scripting environment.

    Args:
        source_or_func (str | Callable): Source code or function to compile.
        globals_dict (dict | None): Optional globals dictionary for execution.
        pvn_alias (str): Name of the imported DSL module.

    Returns:
        Level: The generated level graph object in context.
    """
    import PvZ_Fusion_Node as pvn
    from ..Core.context import ctx

    env = globals_dict.copy() if globals_dict is not None else {}
    env[pvn_alias] = pvn
    env["pvn"] = pvn
    env["PvZ_Fusion_Node"] = pvn
    env["PvzRH_node"] = pvn
    env["ctx"] = ctx

    # Expose common DSL symbols directly into env
    for export_name in pvn.__all__:
        if hasattr(pvn, export_name):
            env[export_name] = getattr(pvn, export_name)

    tree = transpile_to_ast(source_or_func, pvn_alias=pvn_alias)
    compiled_code = compile(tree, filename="<pvz_transpiled>", mode="exec")

    # If source_or_func was a function, executing the compiled code defines the transformed function
    exec(compiled_code, env)

    if callable(source_or_func):
        func_name = source_or_func.__name__
        if func_name in env and callable(env[func_name]):
            # Execute the transformed level function
            env[func_name]()

    return ctx.level


def compile_level(
    *args: Any,
    name: Optional[str] = None,
    output: Optional[str] = None,
    **kwargs: Any,
) -> Any:
    """Decorator or function to compile high-level Python level logic directly into visual graph JSON.

    Usage as decorator:
    ```python
    @pvn.compile_level
    def my_level():
        if pvn.Board.Sun < 100:
            pvn.Board.Sun += 200
        for i in range(5):
            pvn.Spawner.Set_Plant(row=1, col=i, plant_type=pvn.PlantType.Peashooter)
    ```

    Usage with parameters:
    ```python
    @pvn.compile_level(name="ChallengeLevel", output="./Levels")
    def my_level():
        ...
    ```
    """
    from ..Core.context import ctx, Config

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*call_args: Any, **call_kwargs: Any) -> Any:
            ctx.reset()
            if name or output or kwargs:
                cfg_kwargs = {}
                if name:
                    cfg_kwargs["name"] = name
                if output:
                    cfg_kwargs["output"] = output
                cfg_kwargs.update(kwargs)
                Config(**cfg_kwargs)

            # Transpile and execute the function's transformed AST
            func_globals = func.__globals__
            compile_ast(func, globals_dict=func_globals)
            return ctx.level

        return wrapper

    if len(args) == 1 and callable(args[0]):
        return decorator(args[0])
    return decorator
