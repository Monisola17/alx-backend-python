#!/usr/bin/env python3
"""
This module contains a function to calculate the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats and return it as a float.

    Args:
        input_list (List[float]): The input list of float numbers.

    Returns:
        float: The sum of the input list as a float.
    """
    return sum(input_list)
