"""Threads: good for I/O-bound work. Locks protect shared state."""

import threading
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

counter = 0
lock = threading.Lock()


def bump(times: int) -> None:
    global counter
    for _ in range(times):
        with lock:  # without the lock, += is not atomic
            counter += 1


threads = [threading.Thread(target=bump, args=(10_000,)) for _ in range(4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("counter:", counter)


def slow_square(n: int) -> int:
    return n * n


with ThreadPoolExecutor(max_workers=4) as pool:
    print(list(pool.map(slow_square, range(8))))  # results keep input order

# Producer / consumer with a thread-safe queue.
jobs: Queue[int | None] = Queue()
results: list[int] = []


def worker() -> None:
    while (item := jobs.get()) is not None:
        results.append(item * 10)


consumer = threading.Thread(target=worker)
consumer.start()
for number in range(5):
    jobs.put(number)
jobs.put(None)  # sentinel: no more work
consumer.join()
print(results)
