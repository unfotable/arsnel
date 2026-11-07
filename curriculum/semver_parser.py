"""A tiny Semantic Versioning (SemVer) parser: parse, compare and bump.

SemVer is MAJOR.MINOR.PATCH. Increase MAJOR for breaking changes, MINOR for
new backwards-compatible features and PATCH for bug fixes.
"""

import re
from typing import NamedTuple

PATTERN = re.compile(
    r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<pre>[0-9A-Za-z.-]+))?$"
)


class Version(NamedTuple):
    """A parsed version. Tuples compare field by field, which is what we want."""

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def bump(self, part: str) -> "Version":
        """Return the next version for ``part`` ('major', 'minor' or 'patch')."""
        if part == "major":
            return Version(self.major + 1, 0, 0)
        if part == "minor":
            return Version(self.major, self.minor + 1, 0)
        if part == "patch":
            return Version(self.major, self.minor, self.patch + 1)
        raise ValueError(f"unknown part: {part!r}")


def parse(text: str) -> Version:
    """Parse ``text`` (pre-release tags are validated but ignored here)."""
    match = PATTERN.match(text)
    if match is None:
        raise ValueError(f"not a valid SemVer string: {text!r}")
    return Version(int(match["major"]), int(match["minor"]), int(match["patch"]))


current = parse("1.4.2")
print("current  :", current)
for part in ("patch", "minor", "major"):
    print(f"bump {part:<5}:", current.bump(part))

# Compare numerically - as strings "1.10.0" < "1.9.0" would be WRONG.
print("'1.10.0' < '1.9.0' as text   :", "1.10.0" < "1.9.0")
print("1.10.0 < 1.9.0 as versions   :", parse("1.10.0") < parse("1.9.0"))

releases = ["1.0.0", "0.9.1", "1.10.0", "1.2.0", "0.10.0"]
print("sorted   :", [str(v) for v in sorted(map(parse, releases))])

for bad in ("1.2", "01.2.3", "v1.2.3", "1.2.3.4"):
    try:
        parse(bad)
    except ValueError as exc:
        print("rejected :", exc)

# Version specifiers in pyproject.toml use the same ordering: ">=1.2,<2".
print(
    "compatible with '>=1.2,<2'? 1.10.0 ->",
    Version(1, 2, 0) <= parse("1.10.0") < Version(2, 0, 0),
)
