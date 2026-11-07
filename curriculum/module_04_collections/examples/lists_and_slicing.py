"""Lists: mutation, slicing and sorting with a key function."""

# Lists are MUTABLE: methods change the object in place and return None.
numbers = [5, 3, 8, 1]
numbers.append(9)
numbers.extend([2, 7])
numbers.insert(0, 4)
print("after edits:", numbers)

popped = numbers.pop()  # removes and returns the last item
print("popped:", popped, "->", numbers)

# Slicing is [start:stop:step]; stop is exclusive and a slice is a NEW list.
print("first three:", numbers[:3])
print("last two:   ", numbers[-2:])
print("every other:", numbers[::2])
print("reversed:   ", numbers[::-1])

# sorted() returns a new list, list.sort() sorts in place (and returns None).
print("sorted:     ", sorted(numbers))
numbers.sort(reverse=True)
print("sorted desc:", numbers)

# The key= function maps each item to the value used for comparing.
words = ["pear", "Fig", "banana", "kiwi", "apple"]
print("by length:  ", sorted(words, key=len))
print("ignore case:", sorted(words, key=str.lower))

# Sort records by one field, then break ties with a second (tuple keys).
people = [("Ada", 36), ("Linus", 28), ("Grace", 36), ("Guido", 28)]
by_age_then_name = sorted(people, key=lambda p: (-p[1], p[0]))
print("age desc, name asc:", by_age_then_name)

# Common gotcha: the mutator returns None, so this loses your list.
oops = [3, 1, 2].sort()
print("sort() returned:", oops)

# Membership on a list is O(n); the cost grows with the list.
print("4 in numbers?", 4 in numbers)
