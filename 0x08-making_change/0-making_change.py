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
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
