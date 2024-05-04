#!/usr/bin/python3
""" The coin change problem solution
"""
from typing import List
import math


def makeChange(coins: List[int], total: int) -> int:
    """
    solution

    Args:
    coins: array of ints - Available change denoms
    total: int - Money value to find change

    Return: int - Num of coins for change
    """
    def coinChangeInner(rem, cache):
        if rem < 0:
            return math.inf
        if rem == 0:
            return 0
        if rem in cache:
            return cache[rem]
        cache[rem] = min(coinChangeInner(rem-x, cache) + 1 for x in coins)
        return cache[rem]
    ans = coinChangeInner(total, {})
    return -1 if ans == math.inf else ans
