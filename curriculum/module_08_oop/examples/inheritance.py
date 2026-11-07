"""Inheritance, super(), method resolution order, polymorphism and composition."""


class Animal:
    """Base class."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."

    def describe(self) -> str:
        return f"{self.name} says {self.speak()}"


class Dog(Animal):
    def speak(self) -> str:  # override
        return "woof"


class Puppy(Dog):
    def __init__(self, name: str) -> None:
        super().__init__(name)  # reuse the parent's setup
        self.age = 0

    def speak(self) -> str:
        return super().speak() + "!"


for animal in (Animal("thing"), Dog("rex"), Puppy("bit")):  # polymorphism
    print(animal.describe())
print([cls.__name__ for cls in Puppy.__mro__])
print(isinstance(Puppy("p"), Animal), issubclass(Dog, Animal))


# Composition: "has a" is often better than "is a".
class Engine:
    def start(self) -> str:
        return "vroom"


class Car:
    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> str:
        return f"car goes {self.engine.start()}"


print(Car().start())
