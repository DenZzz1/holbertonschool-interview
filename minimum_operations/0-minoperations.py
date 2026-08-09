#!/usr/bin/python3
"""Module that defines a function to compute minimum operations."""


def minOperations(n):
    """Calculate fewest H-Copy/Paste operations to reach n characters.

    Args:
        n (int): the target number of H characters.

    Returns:
        int: the minimum number of operations, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
