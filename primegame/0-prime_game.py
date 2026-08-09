#!/usr/bin/python3
"""Module that defines a function to determine the winner of Prime Game."""


def sieve_of_eratosthenes(n):
    """Return a list of booleans indicating primality up to n.

    Args:
        n (int): the upper bound.

    Returns:
        list: list of booleans where index i is True if i is prime.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False if n >= 1 else is_prime[0]

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    return is_prime


def isWinner(x, nums):
    """Determine who wins the most rounds of the Prime Game.

    Args:
        x (int): the number of rounds.
        nums (list): list of integers representing n for each round.

    Returns:
        str: the name of the player with the most wins, or None if tied.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
        elif prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
