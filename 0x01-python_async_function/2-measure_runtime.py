#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay) -> float:
    """
    Args:
        n - int
        max_delay - int
    Returns:
        total_time / n
    """
    current_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - current_time) / n
