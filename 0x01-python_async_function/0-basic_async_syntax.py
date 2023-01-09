#!/usr/bin/env python3
"""
0-basic_async_syntax
"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument
    named wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it
    """
    dlay: float = uniform(0, max_delay)
    await sleep(dlay)

    return dlay
