"""Async generators, queues and error handling with gather."""

import asyncio
from collections.abc import AsyncIterator


async def ticker(count: int) -> AsyncIterator[int]:
    for i in range(count):
        await asyncio.sleep(0)
        yield i


async def explode() -> None:
    raise ValueError("boom")


async def main() -> None:
    print([n async for n in ticker(4)])

    queue: asyncio.Queue[int | None] = asyncio.Queue()
    seen: list[int] = []

    async def consumer() -> None:
        while (item := await queue.get()) is not None:
            seen.append(item * 2)

    task = asyncio.create_task(consumer())
    for n in range(4):
        await queue.put(n)
    await queue.put(None)
    await task
    print(seen)

    outcomes = await asyncio.gather(
        explode(), asyncio.sleep(0, "fine"), return_exceptions=True
    )
    print([repr(o) for o in outcomes])


asyncio.run(main())
