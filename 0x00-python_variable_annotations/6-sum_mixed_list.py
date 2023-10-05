#!/usr/bin/env python3
"""
This module contains a function to calculate
the sum of a mixed list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers
    and floats and return it as a float.
    Returns:
        float: The sum of the input list as a float.
    """
    return sum(mxd_lst)
