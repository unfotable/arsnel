"""Classes: instances, attributes, methods, properties and class-level members."""


class Player:
    """A game player; ``count`` is shared by the whole class."""

    count = 0  # class attribute

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name  # instance attributes
        self._health = health
        Player.count += 1

    @property
    def health(self) -> int:
        """Read-only view with validation on write."""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, min(100, value))

    def hit(self, damage: int) -> None:
        """Methods receive the instance as ``self``."""
        self.health = self.health - damage

    @classmethod
    def from_string(cls, text: str) -> "Player":
        """Alternative constructor: ``"ada:80"``."""
        name, _, health = text.partition(":")
        return cls(name, int(health))

    @staticmethod
    def is_valid_name(name: str) -> bool:
        """Utility that needs neither the class nor an instance."""
        return name.isalpha()


ada = Player("ada")
grace = Player.from_string("grace:30")
ada.hit(130)
grace.hit(5)
print(ada.name, ada.health, grace.name, grace.health)
print(Player.count, Player.is_valid_name("ada"), Player.is_valid_name("r2d2"))
print(type(ada).__name__, isinstance(ada, Player), ada.__dict__)
