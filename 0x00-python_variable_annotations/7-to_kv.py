#!/usr/bin/env python3
"""
This module contains a function to create a tuple
from a string and the square of an int/float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of an int/float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string `k`
        and the square of `v` as a float.
    """
    return k, float(v ** 2)
