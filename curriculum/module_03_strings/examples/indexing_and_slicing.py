"""Strings are immutable sequences: index, slice and iterate them."""

word = "pythonista"
print(word[0], word[-1], word[2:6], word[:3], word[3:], word[::2], word[::-1])
print(len(word), "thon" in word, word.index("n"))

try:
    word[0] = "P"  # type: ignore[index]
except TypeError as exc:
    print("TypeError:", exc)

# "Changing" a string builds a new one.
print("P" + word[1:])

for position, char in enumerate("abc"):
    print(position, char, ord(char))
print(chr(97), "caf\u00e9".upper(), len("caf\u00e9"), len("caf\u00e9".encode("utf-8")))
print(b"abc".decode(), "h\u00e9".encode("utf-8"))
