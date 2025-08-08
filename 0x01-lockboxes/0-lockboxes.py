#!/usr/bin/python3
""" check if all boxes can be unlocked """
from collections import deque


def canUnlockAll(boxes):
    """ check if all boxes can be unlocked """
    queue = deque([0])
    visited = []

    are_all_unlocked = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for i in boxes[node]:
                if i not in visited:
                    queue.append(i)
            are_all_unlocked.append(True)

    # print(are_all_unlocked)
    # print(visited)
    return len(are_all_unlocked) == len(boxes)
