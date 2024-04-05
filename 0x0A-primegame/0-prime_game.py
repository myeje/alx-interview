#!/usr/bin/python3
"""
Prime game
"""

def isWinner(x, nums):
    """
    this code determines the winner of each round of the prime game.

    x (int): Amount of rounds.
    nums (list): List of integers representing n for each round.

    Returns:
    str or None
    """
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def count_primes(n):
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    def winner(n):
        if n % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    prime_counts = [count_primes(n) for n in nums]

    round_winners = [winner(count) for count in prime_counts]

    maria_wins = round_winners.count("Maria")
    ben_wins = round_winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
