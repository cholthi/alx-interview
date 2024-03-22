#!/usr/bin/python3
""" Minimum operations implemented in Python """


def minOperations(n):
    """ find minimum number of operations needed to have n H """
    if type(n) is not int or n < 0:
        return 0

    if n == 1:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
