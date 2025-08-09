#!/usr/bin/python3
""" check if all boxes can be unlocked """
from collections import deque


def canUnlockAll(boxes):
    """
    boxes: list of lists with keys to other boxes
    Return True if you can open all boxes, else False
    """
    visited = []
    queue = deque([0])
    are_all_unlocked = []

    while queue:
        node = queue.popleft()
        if node not in visited:

            visited.append(node)
            if node < len(boxes):

                for i in boxes[node]:
                    if i not in visited:
                        queue.append(i)

                are_all_unlocked.append(True)
    # print(len(are_all_unlocked))
    # print(len(boxes))
    return len(are_all_unlocked) == len(boxes)
