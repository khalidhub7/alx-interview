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
    clipboard = ['H']
    new_n = n

    while new_n > 1:
        divisor = 2
        while divisor <= new_n:
            if new_n % divisor == 0:
                operations += divisor
                new_n = new_n // divisor
                clipboard = clipboard * divisor
                break
            divisor += 1
    print(clipboard)
    return operations
