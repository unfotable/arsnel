"""Module 08 content: OOP: classes, dunders, inheritance, dataclasses and protocols."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=8,
    intro="Objects bundle data with the behaviour that belongs to it. You will build classes, make them behave like built-ins with dunder methods, reuse code through inheritance and composition, and cut boilerplate with dataclasses and protocols.",
    lessons=(
        Lesson(
            "Classes and instances",
            """
```python
class Player:
    count = 0                       # class attribute (shared)

    def __init__(self, name: str) -> None:
        self.name = name            # instance attribute
        Player.count += 1

    def greet(self) -> str:         # method: first parameter is the instance
        return f"I am {self.name}"
```

`@property` exposes computed or validated attributes, `@classmethod` receives the class (alternative constructors),
`@staticmethod` receives neither. A leading underscore (`_health`) means *internal by convention*.
""",
        ),
        Lesson(
            "Dunder methods",
            """
| Method | Enables |
| --- | --- |
| `__repr__` / `__str__` | debugging / pretty printing |
| `__eq__`, `__lt__`, `__hash__` | `==`, sorting, sets and dict keys |
| `__add__`, `__mul__` | `a + b`, `a * 3` |
| `__len__`, `__getitem__`, `__iter__` | `len(x)`, `x[i]`, `for` loops |
| `__bool__`, `__call__` | truthiness, calling an instance |

If you define `__eq__`, also define `__hash__` (or set it to `None`). `functools.total_ordering` fills in the
other comparisons from `__eq__` and `__lt__`.
""",
        ),
        Lesson(
            "Inheritance and composition",
            """
```python
class Dog(Animal):
    def speak(self) -> str:
        return super().speak() + " woof"
```

`super()` calls the next class in the **MRO** (method resolution order, see `Class.__mro__`).
Polymorphism: code that calls `animal.speak()` works for every subclass.
Prefer **composition** ("has a") over deep inheritance trees ("is a") when you only want to reuse behaviour.
""",
        ),
        Lesson(
            "Dataclasses, ABCs and Protocols",
            """
```python
@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int = 0

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Drawable(Protocol):
    def draw(self) -> str: ...
```

`@dataclass` writes `__init__`, `__repr__`, `__eq__` (and ordering) for you; use `field(default_factory=list)` for
mutable defaults. An **ABC** forces subclasses to implement methods; a **Protocol** is *structural* typing -
anything with the right methods qualifies, no inheritance needed.
""",
        ),
    ),
    examples=(
        Example(
            "classes_basics.py",
            "Classes basics",
            "Attributes, properties, classmethods and staticmethods.",
        ),
        Example("dunders.py", "Dunder methods", "Make objects behave like built-ins."),
        Example(
            "inheritance.py",
            "Inheritance and composition",
            "super(), MRO and polymorphism.",
        ),
        Example(
            "dataclasses_protocols.py",
            "Dataclasses, Protocols, ABCs",
            "Less boilerplate and clearer contracts.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_bank_account.py",
            "Bank account",
            "validation, a property and a custom exception.",
            2,
        ),
        Exercise(
            "ex_02_vector.py",
            "A 2D vector",
            "dunder methods for arithmetic and equality.",
            2,
        ),
        Exercise(
            "ex_03_shapes.py", "Shapes", "dataclasses, an ABC and polymorphism.", 2
        ),
    ),
    quiz=(
        Question(
            "What is `self`?",
            (
                "A keyword",
                "The instance the method is called on",
                "The class",
                "A module",
            ),
            1,
            "It is the conventional name of the first parameter, bound to the instance.",
        ),
        Question(
            "What is the difference between `__repr__` and `__str__`?",
            (
                "None",
                "repr is for developers, str for readable output",
                "str is for developers",
                "repr only works on ints",
            ),
            1,
            "repr should be unambiguous; str is user friendly.",
        ),
        Question(
            "What does `@classmethod` receive as its first argument?",
            ("The instance", "The class", "Nothing", "The module"),
            1,
            "By convention called cls.",
        ),
        Question(
            "Why avoid `members: list = []` in a dataclass?",
            (
                "It is slow",
                "The default would be shared; use field(default_factory=list)",
                "Lists are banned",
                "It breaks repr",
            ),
            1,
            "Dataclasses reject mutable defaults for exactly that reason.",
        ),
        Question(
            "Which gives structural (duck) typing?",
            ("abc.ABC", "typing.Protocol", "@dataclass", "__slots__"),
            1,
            "A Protocol matches any object with the required methods.",
        ),
        Question(
            "If you define `__eq__`, what should you also consider defining?",
            ("__len__", "__hash__", "__del__", "__new__"),
            1,
            "Objects that compare equal must hash equal if they are hashable.",
        ),
        Question(
            "What does `super().__init__(name)` do?",
            (
                "Creates a new class",
                "Runs the parent class initialiser",
                "Deletes the parent",
                "Copies the instance",
            ),
            1,
            "It delegates setup to the next class in the MRO.",
        ),
    ),
    cheatsheet=(
        "`class A(Base):` + `super().__init__()`",
        "`@property`, `@classmethod`, `@staticmethod`",
        "`__repr__ __str__ __eq__ __lt__ __hash__ __len__ __iter__`",
        "`@dataclass(frozen=True, order=True)`",
        "`ABC` + `@abstractmethod`; `Protocol` for duck typing",
        "prefer composition to deep inheritance",
    ),
    next_steps="Next: lazy sequences with iterators and generators in module 09.",
)
