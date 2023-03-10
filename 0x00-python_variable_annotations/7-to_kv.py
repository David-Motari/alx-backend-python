#!/usr/bin/env python3
"""7-to_kv """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        -takes a string k
        - and an int OR float v as arguments
    Returns a tuple.
    """
    return (k, v ** 2)
