#!/bin/usr/env python3
"""
1-async-comprehension
"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    takes 10 random numbers and returns a list
    """
    return [i async for i in async_generator()]
