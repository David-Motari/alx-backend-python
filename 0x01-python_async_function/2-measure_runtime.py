#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n - int
        max_delay - int
    Returns:
        total_time / n
    """
    current_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - current_time) / n
