"""Annotations and warning decorators for experimental and obsolete engine features."""

import functools
import warnings
from typing import Any, Callable, TypeVar, overload

F = TypeVar("F", bound=Callable[..., Any])


class ExperimentalWarning(UserWarning):
    """Warning emitted when using an experimental node or extension feature."""

    pass


class ObsoleteWarning(DeprecationWarning):
    """Warning emitted when using an obsolete or deprecated node or extension feature."""

    pass


@overload
def experimental(arg: F) -> F: ...


@overload
def experimental(arg: str) -> Callable[[F], F]: ...


def experimental(arg: Any = None) -> Any:
    """Decorator marking a function or class as experimental (unverified in-game behavior)."""
    default_msg = "This feature or node lowering is experimental and unverified against in-game engine behavior."

    if callable(arg):
        fn = arg

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(f"{fn.__qualname__}: {default_msg}", category=ExperimentalWarning, stacklevel=2)
            return fn(*args, **kwargs)

        return wrapper

    msg = arg if isinstance(arg, str) else default_msg

    def decorator(fn: F) -> F:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(f"{fn.__qualname__}: {msg}", category=ExperimentalWarning, stacklevel=2)
            return fn(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator


@overload
def Obsolete(arg: F) -> F: ...


@overload
def Obsolete(arg: str) -> Callable[[F], F]: ...


def Obsolete(arg: Any = None) -> Any:
    """Decorator marking a function or class as obsolete / deprecated."""
    default_msg = "This feature or node is obsolete in the engine."

    if callable(arg):
        fn = arg

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(f"{fn.__qualname__}: {default_msg}", category=ObsoleteWarning, stacklevel=2)
            return fn(*args, **kwargs)

        return wrapper

    msg = arg if isinstance(arg, str) else default_msg

    def decorator(fn: F) -> F:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(f"{fn.__qualname__}: {msg}", category=ObsoleteWarning, stacklevel=2)
            return fn(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator


obsolete = Obsolete
