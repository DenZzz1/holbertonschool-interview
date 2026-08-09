#!/usr/bin/python3
"""
Main module for the makeChange function
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize the DP array with an impossible high value (total + 1)
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[total] if dp[total] != total + 1 else -1
