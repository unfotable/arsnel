"""Ways to import, the module namespace and __name__."""

import math
import os.path as osp
from collections import Counter  # noqa: F401 - alias demo
from math import pi, sqrt

print(math.floor(2.7), pi, sqrt(16), osp.basename("/a/b/c.txt"))
print(Counter("banana").most_common(1))

# Every module is an object with a namespace.
print(math.__name__, type(math).__name__, hasattr(math, "sqrt"))
print("__name__ in this file:", __name__)


def main() -> None:
    """Code under the main guard runs only when executed, not when imported."""
    print("running as a script")


if __name__ == "__main__":
    main()
