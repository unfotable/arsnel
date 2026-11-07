"""Dicts in depth: methods, defaultdict and Counter."""

from collections import Counter, defaultdict

# Dicts keep INSERTION order and map unique, hashable keys to values.
stock = {"apple": 3, "pear": 0}
stock["fig"] = 12  # add
stock["apple"] += 2  # update
print("stock:", stock)

# [] raises KeyError for a missing key; .get() lets you supply a default.
print("kiwi:", stock.get("kiwi", "n/a"))
print("setdefault:", stock.setdefault("kiwi", 1), "->", stock)

# Iterate with .items(); merge with | (3.9+).
for name, qty in stock.items():
    if qty == 0:
        print(f"  out of {name}")
merged = stock | {"apple": 100, "plum": 7}
print("merged apple/plum:", merged["apple"], merged["plum"])

# pop removes a key; the second argument avoids KeyError.
print("pop pear:", stock.pop("pear"), "| pop nope:", stock.pop("nope", None))

# defaultdict creates missing values on demand - perfect for grouping.
words = ["tea", "eat", "ate", "tan", "nat", "bat"]
groups: defaultdict[str, list[str]] = defaultdict(list)
for word in words:
    groups["".join(sorted(word))].append(word)
print("anagram groups:", dict(groups))

# Counter is a dict subclass specialised for tallies.
text = "the cat and the hat and the bat"
counts = Counter(text.split())
print("counts:", counts)
print("top 2:", counts.most_common(2))
print("missing word:", counts["dog"])  # 0, never KeyError

# Counters support arithmetic.
print("sum:", Counter("aab") + Counter("abc"))

# Invert a mapping with a dict comprehension (values must be unique).
codes = {"a": 1, "b": 2}
print("inverted:", {v: k for k, v in codes.items()})
