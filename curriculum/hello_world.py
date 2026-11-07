"""Your first Python program: print(), comments and a few tricks."""

# A comment starts with '#'. Python ignores it; humans read it.
print("Hello, ARSNEL!")

# print() accepts many values and joins them with a space.
print("one", "two", "three")

# `sep` changes the separator, `end` changes what comes after the text.
print("a", "b", "c", sep="-")
print("no newline here", end=" <- ")
print("see?")

# Triple-quoted strings can span several lines.
print("""> terminal
$ python hello_world.py
Hello!""")

# Python is evaluated top to bottom, one statement at a time.
print("done", "✓")
