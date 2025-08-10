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
        current_len = len(queue)
        if current_len == n:
            break

        if (current_len * 2) <= n:
            queue.extend(queue)
            operations += 2  # copy all + paste
            clipboard_history.append(''.join(queue))

        else:
            rest = n - current_len

            for i in reversed(clipboard_history):
                if len(i) == rest:
                    queue.extend(i)  # paste
                    operations += 1
                    break
                else:
                    if len(i) < rest:
                        queue.extend(i)  # paste
                        operations += 1
                        rest -= len(i)
    # print(clipboard_history)
    return operations
