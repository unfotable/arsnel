"""The string methods you will use every day."""

text = "  The quick brown fox  "
print(repr(text.strip()), text.lower().strip(), text.title().strip())
print(text.strip().split(), "-".join(["a", "b", "c"]))
print(["a", "b", "", "c"], ["a", "b,c"])
print("banana".count("an"), "banana".find("na"), "banana".find("zz"))
print("banana".replace("a", "o"), "banana".startswith("ban"), "x.py".endswith(".py"))
print("42".isdigit(), "abc".isalpha(), "ab1".isalnum(), "  ".isspace())
print("hello".center(11, "*"), "7".zfill(3), "ab".ljust(5, ".") + "|")
print("line1\nline2".splitlines(), "a b".partition(" "))

# Raw strings keep backslashes: handy for regular expressions and Windows paths.
print(r"C:\new\table", "C:\\new\\table")
