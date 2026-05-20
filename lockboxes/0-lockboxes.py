#!/usr/bin/python3
"""Module for lockboxes problem."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes: list of lists, each containing keys to other boxes

    Returns:
        True if all boxes can be opened, False otherwise
    """
    unlocked = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)
