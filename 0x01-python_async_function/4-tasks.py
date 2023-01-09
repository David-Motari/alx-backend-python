#!/usr/bin/env python3
"""
4-tasks
"""
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    clone of task 1
    """
    dlayLst: List[float] = []
    tskList: List[asyncio.Task] = []

    for i in range(n):
        tskList.append(task_wait_random(max_delay))

    for tsk in asyncio.as_completed((tskList)):
        dlay = await tsk
        dlayLst.append(dlay)

    return dlayLst
