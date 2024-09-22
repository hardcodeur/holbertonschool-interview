#!/usr/bin/python3
"""
This function calculates the minimum number of operations
required to get exactly `n` characters 'H' in a file, starting with one 'H'.
Operations allowed: 'Copy All' and 'Paste'.
"""

def minOperations(n) :
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required, or 0 if n <= 1.

    The algorithm works by breaking down the target number n into its prime factors.
    For each prime factor, it calculates the number of operations as the sum of
    those factors (representing a sequence of "Copy All" and "Paste" operations).
    """
    if n <= 1 :
        return 0
    
    steps = 0
    divisor = 2

    while n > 1 :
        while n % divisor == 0 : 
            steps =  steps + divisor
            n = n / divisor
        divisor = divisor + 1
        
    return steps           
