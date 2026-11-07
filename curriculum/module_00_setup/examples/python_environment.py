"""Ask Python about itself: version, interpreter, platform and search path.

The output differs on every machine, and that is the point: this is how you
find out *which* Python you are really running.
"""

import platform
import sys

print(f"Python version : {platform.python_version()}")
print(f"Version tuple  : {sys.version_info[:3]}")
print(f"Implementation : {platform.python_implementation()}")
print(f"Interpreter    : {sys.executable}")
print(f"System         : {platform.system()} ({sys.platform})")

# Inside a virtual environment, sys.prefix points at the venv while
# sys.base_prefix still points at the Python that created it.
in_venv = sys.prefix != sys.base_prefix
print(f"Inside a venv? : {in_venv}")

# Tuples compare element by element - the right way to check versions.
if sys.version_info >= (3, 11):  # noqa: UP036 - teaching version tuples
    print("Version check  : OK, 3.11 or newer")
else:
    print("Version check  : too old, ARSNEL needs Python 3.11+")

# Python looks for imports in these folders, in this order.
print("First import-search entries:")
for entry in sys.path[:3]:
    print(f"  {entry!r}")
