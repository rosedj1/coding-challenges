"""Return True if a number is evenly divisible by 3.

Author: Dr. Jake Rosenzweig
Date: 2023-11-11, Happy 12th Anniversary, Skyrim!

Challenge: Divisible by 3
Difficulty: 3/10
URL: https://pythonprinciples.com/challenges/Divisible-by-3/

Define a function named div_3 that returns True if its single-integer
parameter is divisible by 3 and False otherwise.

For example, div_3(6) is True because 6/3 does not leave any remainder.
However div_3(5) is False because 5/3 leaves 2 as a remainder.

Performance Testing:
====================
# Jake's Solution:
>>> %timeit div_3(6)
80.5 ns ± 0.335 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> %timeit div_3_egsoln(6)
75.4 ns ± 0.0774 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* Don't bog your code down with a bunch of True's or False's;
    - Instead, let the comparisons (e.g., n % 3 == 0) give you the bool.
"""
def div_3(n):
    """Return True if n is evenly divisible by 3."""
    return True if n % 3 == 0 else False

def div_3_egsoln(n):
    """Return True if n is evenly divisible by 3."""
    return n % 3 == 0

if __name__ == '__main__':
    print("Jake's solution:")
    print(f"Should return True: {div_3(6)}")
    print(f"Should return False: {div_3(7)}")
    print("Example solution:")
    print(f"Should return True: {div_3_egsoln(6)}")
    print(f"Should return False: {div_3_egsoln(7)}")