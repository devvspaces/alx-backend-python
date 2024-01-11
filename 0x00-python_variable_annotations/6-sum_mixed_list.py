#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return sum of list of floats and ints"""
    return float(sum(mxd_list))
