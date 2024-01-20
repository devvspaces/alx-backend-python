#!/usr/bin/env python3

"""Let's execute multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def run(response: List[int], max_delay: int) -> None:
    """Run function"""
    wait = await wait_random(max_delay)
    response.append(wait)


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Wait for random time"""
    responses = []
    tasks = []
    for _ in range(n):
        tasks.append(run(responses, max_delay))
    await asyncio.gather(*tasks)
    return responses


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
