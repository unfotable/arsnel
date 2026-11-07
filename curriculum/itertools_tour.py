"""itertools: building blocks for iteration."""

import itertools as it
from collections import Counter

print(list(it.chain([1, 2], "ab", (9,))))
print(list(it.islice(it.count(10, 5), 4)), list(it.islice(it.cycle("xy"), 5)))
print(list(it.accumulate([1, 2, 3, 4])), list(it.pairwise("abcd")))
print(list(it.product("ab", [1, 2])))
print(list(it.permutations("abc", 2)))
print(list(it.combinations("abcd", 2)))
print(list(it.zip_longest("ab", [1, 2, 3], fillvalue="-")))
print(list(it.repeat("z", 3)), list(it.takewhile(lambda n: n < 4, range(10))))

words = sorted(["apple", "avocado", "banana", "blueberry", "cherry"])
for letter, group in it.groupby(words, key=lambda w: w[0]):  # input must be sorted
    print(letter, list(group))
print(Counter(len(w) for w in words))
