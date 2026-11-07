"""Reading and writing files: open(), ``with``, modes, text vs binary, encodings."""

import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "notes.txt"

    # "w" creates or TRUNCATES. Always pass encoding= for portable text files.
    # newline="\n" keeps the bytes identical on every operating system.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("first line\n")
        fh.write("café ☕\n")
        fh.writelines(["third\n", "fourth\n"])
    # Leaving the ``with`` block closes the file, even if an error happened.

    # Reading: read() = everything, readline() = one line, iteration = lazy lines.
    with open(path, encoding="utf-8") as fh:
        print("first line :", repr(fh.readline()))
        print("rest       :", fh.read().splitlines())

    with open(path, encoding="utf-8") as fh:
        for number, line in enumerate(fh, start=1):  # one line in memory at a time
            print(f"{number}: {line.rstrip()}")

    # "a" appends; "x" refuses to overwrite an existing file.
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        fh.write("appended\n")
    try:
        open(path, "x", encoding="utf-8").close()
    except FileExistsError:
        print("mode 'x' refused to overwrite an existing file")

    # Text vs binary: text mode gives str, "rb"/"wb" give bytes.
    raw = path.read_bytes()
    print("bytes type :", type(raw).__name__, "| first 10:", raw[:10])
    print("decoded ok :", raw.decode("utf-8").splitlines()[1])

# Encodings turn characters into bytes. The same text, different byte counts:
text = "café ☕"
print(f"{len(text)} characters")
for encoding in ("utf-8", "utf-16", "latin-1"):
    try:
        print(f"{encoding:8}-> {len(text.encode(encoding))} bytes")
    except UnicodeEncodeError:
        print(f"{encoding:8}-> cannot encode the coffee cup")

# Decoding with the wrong codec gives mojibake (or an error):
print("wrong codec:", "café".encode().decode("latin-1"))
