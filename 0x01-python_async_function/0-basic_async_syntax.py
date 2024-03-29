#!/usr/bin/env python3

"""The basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random time"""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait


if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
