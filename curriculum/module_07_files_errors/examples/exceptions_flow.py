"""try / except / else / finally: the full control flow of exception handling."""


def parse_ratio(text: str) -> float:
    """Return ``a/b`` for text like ``"6/3"``; shows every clause of try."""
    print(f"  parse_ratio({text!r})")
    try:
        left, right = text.split("/")
        result = int(left) / int(right)
    except ValueError as exc:  # bad number OR wrong number of parts
        print("  except ValueError:", exc)
        return float("nan")
    except ZeroDivisionError:
        print("  except ZeroDivisionError")
        return float("inf")
    else:
        # Runs only when NO exception happened; keeps the try block small.
        print("  else: success")
        return result
    finally:
        # Always runs - even though the branches above all return.
        print("  finally: cleanup")


for sample in ["6/3", "6/0", "six/3", "1/2/3"]:
    print(parse_ratio(sample))

# Handlers are checked top to bottom: put specific errors before general ones.
for value in [{"a": 1}, [1], None]:
    try:
        print(value["a"] if isinstance(value, dict) else value[5])  # type: ignore[index]
    except (KeyError, IndexError) as exc:  # several types in one clause
        print("lookup failed:", type(exc).__name__)
    except TypeError as exc:
        print("type problem:", exc)

# All built-in exceptions form a tree; catching a parent catches its children.
print(issubclass(KeyError, LookupError), issubclass(FileNotFoundError, OSError))

# Re-raise after logging with a bare ``raise`` (keeps the original traceback).
try:
    try:
        int("x")
    except ValueError:
        print("logging the problem...")
        raise
except ValueError as exc:
    print("caller still sees:", exc)
