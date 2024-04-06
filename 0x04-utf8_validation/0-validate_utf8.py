#!/usr/bin/python3
""" Provides a function to validate if data is in
valid utf-8 encoding"""


def validUTF8(data):
    """validates if data is valid utf-8 encoding"""
    n_bytes = 0
    for b in data:
        if n_bytes > 0:
            if b >> 6 != 0b10:
                return False
            n_bytes -= 1
        else:
            if b >> 7 == 0:
                n_bytes = 0
            elif b >> 5 == 0b110:
                n_bytes = 1
            elif b >> 4 == 0b1110:
                n_bytes = 2
            elif b >> 3 == 0b11110:
                n_bytes = 3
            else:
                return False
    return n_bytes == 0
