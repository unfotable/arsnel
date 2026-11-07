"""Module 11 content: async/await, threads and multiprocessing."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=11,
    intro="Waiting is wasted time. You will learn when to reach for threads, asyncio or processes - the choice depends on whether your program waits on I/O or burns CPU - and how to keep shared state safe.",
    lessons=(
        Lesson(
            "The GIL and choosing a tool",
            """
CPython's **Global Interpreter Lock** lets only one thread run Python bytecode at a time. So:

| Workload | Best tool |
| --- | --- |
| waiting on network/disk (**I/O-bound**), few tasks | threads (`ThreadPoolExecutor`) |
| waiting on network/disk, thousands of tasks | `asyncio` |
| heavy computation (**CPU-bound**) | processes (`ProcessPoolExecutor`) |

Always measure before parallelising; concurrency adds complexity.
""",
        ),
        Lesson(
            "Threads",
            """
```python
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, urls))     # input order preserved
lock = threading.Lock()
with lock:
    shared += 1                               # += is NOT atomic
```

Use `queue.Queue` to pass work between threads, and a sentinel (`None`) to say "no more".
Threads share memory, which is both their strength and the source of race conditions.
""",
        ),
        Lesson(
            "asyncio",
            """
```python
async def fetch(n):
    await asyncio.sleep(0.1)     # hand control back to the event loop
    return n

async def main():
    results = await asyncio.gather(fetch(1), fetch(2))
    async with asyncio.TaskGroup() as group: ...
    async with asyncio.timeout(1): ...

asyncio.run(main())
```

A coroutine only runs when awaited or scheduled. **Never block** inside `async def` (no `time.sleep`, no heavy loops).
`asyncio.Semaphore` bounds concurrency; `async for` consumes async generators.
""",
        ),
        Lesson(
            "Processes",
            """
```python
if __name__ == "__main__":                   # REQUIRED guard
    with ProcessPoolExecutor() as pool:
        totals = list(pool.map(cpu_heavy, chunks))
```

Each process has its own memory and GIL, so CPU work scales across cores. Arguments and results are
**pickled**, so functions must be defined at module level. Startup costs mean tiny tasks are slower than a plain loop.
""",
        ),
    ),
    examples=(
        Example(
            "threads_basics.py",
            "Threads",
            "Locks, pools and a producer/consumer queue.",
        ),
        Example(
            "asyncio_basics.py",
            "asyncio",
            "gather, TaskGroup, timeouts and semaphores.",
        ),
        Example(
            "async_patterns.py",
            "Async patterns",
            "Async generators, queues and gather errors.",
        ),
        Example(
            "processes_basics.py",
            "Processes",
            "CPU-bound work with ProcessPoolExecutor.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_thread_pool.py",
            "Thread pool and counter",
            "parallel_map and a lock-protected counter.",
            2,
        ),
        Exercise(
            "ex_02_async_gather.py",
            "Async gather",
            "run coroutines concurrently and collect errors.",
            3,
        ),
        Exercise(
            "ex_03_process_pool.py", "Process pool", "count primes across processes.", 2
        ),
    ),
    quiz=(
        Question(
            "Which tool suits CPU-bound work in CPython?",
            ("threads", "asyncio", "processes", "none"),
            2,
            "Processes sidestep the GIL.",
        ),
        Question(
            "Why is `counter += 1` unsafe across threads?",
            ("It is slow", "It is not atomic", "It needs asyncio", "It uses processes"),
            1,
            "Read-modify-write can interleave; protect it with a Lock.",
        ),
        Question(
            "What must you never do inside `async def`?",
            (
                "await",
                "Call blocking functions like time.sleep",
                "Return values",
                "Use f-strings",
            ),
            1,
            "Blocking freezes the whole event loop.",
        ),
        Question(
            "What does asyncio.gather return?",
            (
                "A set",
                "A list of results in argument order",
                "The first result",
                "A generator",
            ),
            1,
            "Results keep the order of the awaitables.",
        ),
        Question(
            'Why do multiprocessing scripts need `if __name__ == "__main__":`?',
            (
                "Style",
                "Child processes re-import the module",
                "It is faster",
                "Windows only",
            ),
            1,
            "Without the guard, children would start more children.",
        ),
        Question(
            "What does `asyncio.run(main())` do?",
            (
                "Starts a thread",
                "Creates an event loop, runs main, closes it",
                "Imports asyncio",
                "Blocks forever",
            ),
            1,
            "It is the standard entry point for async programs.",
        ),
        Question(
            "What is a sentinel in a worker queue?",
            ("A lock", "A special value meaning no more work", "A thread", "A timeout"),
            1,
            "Often None, it tells consumers to stop.",
        ),
    ),
    cheatsheet=(
        "I/O-bound: threads or asyncio; CPU-bound: processes",
        "`ThreadPoolExecutor.map`, `threading.Lock`, `queue.Queue`",
        "`async def` / `await` / `asyncio.run`",
        "`gather`, `TaskGroup`, `timeout`, `Semaphore`",
        "`ProcessPoolExecutor` + `__main__` guard",
        "never block the event loop",
    ),
    next_steps="Next: prove your code works with tests in module 12.",
)
