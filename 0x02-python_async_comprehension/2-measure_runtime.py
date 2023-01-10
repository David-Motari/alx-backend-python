#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    measure total runtime and returns it
    """
    initialTime = time.time()
    load = [async_comprehension() for i in range(4)]
    await asyncio.gather(*load)

    return time.time() - initialTime
