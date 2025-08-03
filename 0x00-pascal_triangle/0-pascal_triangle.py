#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ pascal triangle """
    current = []
    fake = []
    to_remove = 0
    if n <= 0:
        yield current
        return
    for i in range(n):
        if i < 2:
            current.append(1)
            yield current
        else:
            for j in range(len(current) - 1):
                fake.append(current[j] + current[j + 1])

            current = current[:-1] + fake + current[-1:]
            del current[1:1 + to_remove]

            to_remove = len(fake)
            fake = []
            yield current
