"""if / elif / else, the conditional expression and structural pattern matching."""


def grade(score: int) -> str:
    """Return a letter grade; the first matching branch wins."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    return "F"


for s in (95, 85, 72, 10):
    print(s, grade(s))

# Conditional expression.
age = 20
print("adult" if age >= 18 else "minor")


def describe(command: str) -> str:
    """match compares a value against patterns, top to bottom."""
    match command.split():
        case ["quit"]:
            return "bye"
        case ["go", direction]:
            return f"going {direction}"
        case ["take", *items] if items:
            return "taking " + ", ".join(items)
        case _:
            return "unknown command"


for line in ("quit", "go north", "take sword shield", "dance"):
    print(f"{line!r:22} -> {describe(line)}")
