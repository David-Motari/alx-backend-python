#!/usr/bin/env python3
"""
1-concurrent_coroutes
"""
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n - int
        max_delay - int
    Returns:
        the list of all the delays (float values).
    """
    dlayLst: List[float] = []
    tskList: List = []

    for i in range(n):
        tskList.append(wait_random(max_delay))

    for tsk in asyncio.as_completed((tskList)):
        dlay = await tsk
        dlayLst.append(dlay)

    return dlayLst
