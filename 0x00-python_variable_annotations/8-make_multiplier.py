#!/usr/bin/env python3
"""
8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Arg: Multiplier
    Returns function that multiplies a float by a multiplier
    """

    def func(n):
        return n * multiplier

    return func
