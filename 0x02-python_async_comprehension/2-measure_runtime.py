#!/usr/bin/env python3
"""
This module defines a coroutine, `measure_runtime`
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of async_comprehension executed 4 times"""
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - s
