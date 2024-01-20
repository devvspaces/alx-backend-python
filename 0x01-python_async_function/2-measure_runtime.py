#!/usr/bin/env python3

"""Let's execute multiple coroutines at the same time with async"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Wait for random time"""
    now = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter() - now) / n


if __name__ == "__main__":
    print(measure_time(5, 9))
