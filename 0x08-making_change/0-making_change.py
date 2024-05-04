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
    def change(n):
        if F[n] != -1:
            return F[n]
        value = float('inf')
        for coin in coins:
            if coin <= n:
                value = min(change(n-coin), value)
        F[n] = value + 1 if value != -1 else -1
        return F[n]
    if total == 0:
        return 0
    F = [-1 for _ in range(total + 1)]
    F[0] = 0
    change(total)
    return F[-1] if F[-1] != float('inf') else -1
