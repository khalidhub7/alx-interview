#!/usr/bin/python3
"""
minimum operations to get n 'H'
using copy all and paste
"""


def minOperations(n):
    """ return min operations to reach n 'H' """
    if n <= 0:
        return 0

    queue = ['H']
    operations = 0
    clipboard_history = ['H']

    while True:
        node = len(queue)
        if node == n:
            break

        if (node * 2) <= n:
            queue.extend(queue)
            operations += 2  # copy all + paste
            clipboard_history.append(''.join(queue))
        else:
            rest = n - len(queue)
            for i in clipboard_history:
                if len(i) == rest:
                    queue.extend(i)  # paste
                    operations += 1
                    break
    return operations
