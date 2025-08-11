#!/usr/bin/python3
"""
minimum operations to get n 'H'
using copy all and paste
"""


def minOperations(n):
    """ return min operations to reach n 'H' """
    if n <= 1:
        return 0

    operations = 0
    clipboard_len = 1  # start with one 'H'
    new_n = n

    while clipboard_len != n:
        divisor = 2
        while True:
            if new_n % divisor == 0:
                new_n = new_n // divisor
                operations += divisor
                clipboard_len *= divisor
                break
            divisor += 1
    return operations
