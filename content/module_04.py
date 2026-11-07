"""Module 04 content: lists, tuples, sets, dicts and comprehensions."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=4,
    intro=(
        "Real programs juggle collections of things. Python ships four powerful "
        "containers - list, tuple, set and dict - plus comprehensions, a compact "
        "way to build them. Choosing the right container is half of writing good Python."
    ),
    lessons=(
        Lesson(
            "Lists: ordered and mutable",
            """
```python
nums = [3, 1, 2]
nums.append(4); nums.insert(0, 9); nums.remove(1)
nums[1:3]            # slicing -> new list
nums.sort(key=lambda n: -n)
sorted(nums)         # returns a new list, original untouched
```

Lists are **mutable**: methods like `append`, `sort`, `reverse` change the
list in place and return `None`. Slices copy; assignment (`b = a`) only
creates another name for the same list.
""",
        ),
        Lesson(
            "Tuples and sets",
            """
| Type | Ordered | Mutable | Duplicates | Use for |
| --- | --- | --- | --- | --- |
| `list` | yes | yes | yes | sequences of similar things |
| `tuple` | yes | no | yes | fixed records, dict keys |
| `set` | no | yes | no | membership, uniqueness |
| `dict` | insertion | yes | keys unique | lookup by key |

Tuples unpack: `x, y = point`; `first, *rest = items`.
Sets support algebra: `a | b` union, `a & b` intersection, `a - b` difference, `a ^ b` symmetric difference.
""",
        ),
        Lesson(
            "Dictionaries",
            """
```python
ages = {"ada": 36, "linus": 54}
ages["grace"] = 85
ages.get("bob", 0)               # default instead of KeyError
for name, age in ages.items(): ...
```

`collections.defaultdict(list)` creates missing values on demand and
`collections.Counter` counts hashable items. Keys must be hashable
(immutable): strings, numbers and tuples work; lists do not.
""",
        ),
        Lesson(
            "Comprehensions",
            """
```python
squares = [n * n for n in range(10) if n % 2 == 0]
lookup  = {word: len(word) for word in words}
unique  = {w.lower() for w in words}
total   = sum(n * n for n in range(10))     # generator expression: lazy
```

Read them as: *expression, for-clause, optional if-clause*. Keep them short;
if one needs more than one condition and a nested loop, use a normal loop.

**Copies:** `list(a)`, `a[:]`, `a.copy()` are *shallow*; use `copy.deepcopy` when
the container holds other mutable containers.
""",
        ),
    ),
    examples=(
        Example(
            "lists_and_slicing.py",
            "Lists and slicing",
            "Mutation, slicing and sorting with a key function.",
        ),
        Example(
            "tuples_and_sets.py",
            "Tuples and sets",
            "Unpacking, uniqueness and set algebra.",
        ),
        Example(
            "dicts_and_counters.py",
            "Dicts, defaultdict, Counter",
            "Dict methods and the two most useful helpers.",
        ),
        Example(
            "comprehensions.py",
            "Comprehensions",
            "List/set/dict comprehensions and generator expressions.",
        ),
        Example(
            "copying_and_mutation.py",
            "Aliases and copies",
            "Shallow vs deep copies and surprising mutation.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_dedupe_ordered.py",
            "Dedupe, keep order",
            "remove duplicates but keep first occurrences.",
            1,
        ),
        Exercise(
            "ex_02_word_counts.py",
            "Word counts",
            "count words ignoring case and punctuation.",
            2,
        ),
        Exercise("ex_03_group_by.py", "Group by", "bucket items by a key function.", 2),
        Exercise(
            "ex_04_matrix_toolkit.py",
            "Matrix toolkit",
            "transpose and multiply nested lists.",
            3,
        ),
    ),
    quiz=(
        Question(
            "What does `[1, 2, 3].sort()` return?",
            ("[1, 2, 3]", "None", "A new sorted list", "True"),
            1,
            "In-place methods return None; use sorted() for a new list.",
        ),
        Question(
            "Which of these can be a dict key?",
            ("[1, 2]", "{1, 2}", "(1, 2)", "{'a': 1}"),
            2,
            "Keys must be hashable; tuples of hashables are, lists/sets/dicts are not.",
        ),
        Question(
            "`a = [1, 2]; b = a; b.append(3)` - what is `a`?",
            ("[1, 2]", "[1, 2, 3]", "[3]", "An error"),
            1,
            "`b = a` makes a second name for the same list.",
        ),
        Question(
            "What is `{1, 2, 3} & {2, 3, 4}`?",
            ("{2, 3}", "{1, 4}", "{1, 2, 3, 4}", "{2, 3, 4}"),
            0,
            "`&` is set intersection.",
        ),
        Question(
            "What does `[n * n for n in range(4)]` produce?",
            ("[1, 4, 9, 16]", "[0, 1, 4, 9]", "[0, 1, 2, 3]", "[0, 2, 4, 6]"),
            1,
            "range(4) yields 0..3, each squared.",
        ),
        Question(
            "How do you read a missing key without an error?",
            ("d['k']", "d.get('k')", "d.find('k')", "d.k"),
            1,
            "dict.get returns None (or a default) for a missing key.",
        ),
        Question(
            "Which copy is needed for a list of lists so inner lists are independent?",
            ("a[:]", "list(a)", "copy.deepcopy(a)", "a.copy()"),
            2,
            "Slices and .copy() are shallow; deepcopy duplicates nested containers too.",
        ),
    ),
    cheatsheet=(
        "`lst.append/extend/insert/remove/pop`, `sorted(x, key=...)`",
        "`a, *rest = seq` unpacking",
        "`s1 | s2`, `s1 & s2`, `s1 - s2`",
        "`d.get(k, default)`, `d.items()`, `defaultdict`, `Counter`",
        "`[expr for x in it if cond]`, `{k: v for ...}`, `{x for ...}`",
        "`copy.deepcopy` for nested containers",
    ),
    next_steps="Next: package behaviour into reusable functions in module 05.",
)
