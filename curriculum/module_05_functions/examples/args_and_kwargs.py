"""*args collects extra positionals, **kwargs collects extra keywords."""

from typing import Any


def total(*numbers: float) -> float:
    """``numbers`` is a tuple of every positional argument."""
    print("  got", numbers)
    return sum(numbers)


print("total:", total(1, 2, 3))
print("total of nothing:", total())


def build_tag(name: str, **attrs: str) -> str:
    """``attrs`` is a dict of every extra keyword argument."""
    parts = " ".join(f'{key}="{value}"' for key, value in sorted(attrs.items()))
    return f"<{name} {parts}>" if parts else f"<{name}>"


print(build_tag("a", href="/home", title="Home"))
print(build_tag("br"))

# The same stars UNPACK at the call site.
values = [10, 20, 30]
print("unpack list:", total(*values))
options = {"href": "/docs", "rel": "help"}
print("unpack dict:", build_tag("a", **options))

# Merge dicts and extend lists with the same idea.
defaults = {"sep": ", ", "end": "!\n"}
print(*["a", "b", "c"], sep=defaults["sep"], end=defaults["end"])


# A wrapper forwards everything it does not care about.
def logged(func_name: str, *args: Any, **kwargs: Any) -> None:
    """Print how a call would look, then forward-style formatting."""
    shown = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
    print(f"call {func_name}({', '.join(shown)})")


logged("open", "data.txt", mode="r", encoding="utf-8")

# Order in a signature: positional, *args, keyword-only, **kwargs.


def full(a: int, b: int = 2, *rest: int, flag: bool = False, **extra: int) -> str:
    """Every parameter kind in one signature."""
    return f"a={a} b={b} rest={rest} flag={flag} extra={extra}"


print(full(1))
print(full(1, 5, 6, 7, flag=True, x=1))
