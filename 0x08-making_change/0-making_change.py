#!/usr/bin/python3
""" The coin change problem solution
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    solution

    Args:
    coins: array of ints - Available change denoms
    total: int - Money value to find change

    Return: int - Num of coins for change
    """
    dp = [0] + [total + 1] * total
    for coin in coins:
      for i in range(coin, total + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[total] == total + 1 else dp[total]
