"""Exercise 08.1 - Bank account

A class with validation, a property and a custom exception.

Run:  python ex_01_bank_account.py
"""

from __future__ import annotations


class InsufficientFunds(Exception):
    """Raised when a withdrawal exceeds the balance."""


class BankAccount:
    """An account holding whole cents."""

    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> int:
        """Current balance in cents (read-only)."""
        return self._balance

    def deposit(self, amount: int) -> None:
        """Add ``amount`` (> 0) to the balance; raise ValueError otherwise."""
        # TODO: validate amount > 0, then update self._balance.
        raise NotImplementedError("TODO: your turn")

    def withdraw(self, amount: int) -> None:
        """Remove ``amount``; raise InsufficientFunds if it is more than the balance."""
        # TODO: validate amount > 0, check the balance, then update it.
        raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    account = BankAccount("ada", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120
    for bad in (0, -5):
        try:
            account.deposit(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("non-positive deposit must raise ValueError")
    try:
        account.withdraw(1000)
    except InsufficientFunds:
        pass
    else:
        raise AssertionError("overdraft must raise InsufficientFunds")
    assert account.balance == 120, "failed operations must not change the balance"
    try:
        account.balance = 5  # type: ignore[misc]
    except AttributeError:
        pass
    else:
        raise AssertionError("balance must be read-only")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_bank_account: {exc!r}")
    print("PASS ex_01_bank_account")
