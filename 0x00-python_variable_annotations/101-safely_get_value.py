#!/usr/bin/env python3
"""
101-safely_get_value
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, Any] = None
) -> Union[Any, T]:
    """
    Adding annotation to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
