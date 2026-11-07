"""Choose the container that matches your access pattern."""

import bisect
from collections import deque


class Counted:
    """Counts equality comparisons to show how much work a lookup does."""

    comparisons = 0

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        Counted.comparisons += 1
        return isinstance(other, Counted) and self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)


items = [Counted(i) for i in range(1000)]
Counted.comparisons = 0
_ = Counted(999) in items  # list: scans
print("list lookup comparisons:", Counted.comparisons)
as_set = set(items)
Counted.comparisons = 0
_ = Counted(999) in as_set  # set: hash, then one comparison
print("set lookup comparisons :", Counted.comparisons)

queue: deque[int] = deque(range(5))
queue.appendleft(-1)  # O(1) at both ends; list.insert(0, x) is O(n)
print(queue.popleft(), list(queue))

ordered = [10, 20, 30, 40]
bisect.insort(ordered, 25)
print(ordered, bisect.bisect_left(ordered, 30))
