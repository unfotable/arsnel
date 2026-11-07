"""asyncio: cooperative multitasking with async/await."""

import asyncio


async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)  # yields control to the event loop
    return f"{name} done"


async def main() -> None:
    # gather runs coroutines concurrently and keeps the order of the arguments.
    print(await asyncio.gather(fetch("a", 0.03), fetch("b", 0.01), fetch("c", 0.02)))

    # TaskGroup (3.11+) waits for all tasks and propagates errors.
    async with asyncio.TaskGroup() as group:
        first = group.create_task(fetch("x", 0.01))
        second = group.create_task(fetch("y", 0.0))
    print(first.result(), "|", second.result())

    # Timeouts.
    try:
        async with asyncio.timeout(0.01):
            await asyncio.sleep(1)
    except TimeoutError:
        print("timed out")

    # Limit concurrency with a semaphore.
    gate = asyncio.Semaphore(2)
    active = peak = 0

    async def limited(i: int) -> None:
        nonlocal active, peak
        async with gate:
            active += 1
            peak = max(peak, active)
            await asyncio.sleep(0.005)
            active -= 1

    await asyncio.gather(*(limited(i) for i in range(6)))
    print("peak concurrency:", peak)


asyncio.run(main())
