"""Generate a random integer between 1 and 100.

Author: Dr. Jake Rosenzweig
Date: 2023-11-09

Challenge: Randomness
Difficulty: 2/10
URL: https://pythonprinciples.com/challenges/Randomness/

Define a function, random_number, that takes no parameters.
The function must generate a random integer between 1 and 100,
both inclusive, and return it. Calling the function multiple times should
(usually) return different numbers. For example, calling random_number() some
times might first return 42, then 63, then 1.

Performance Testing:
====================
N/A. My solution matched the example solution.

#=======================#
#=== Lessons Learned ===#
#=======================#
* The `random` module is nice. :-)
"""
from random import randint

def random_number():
    """Return a random integer between 1 and 100 (inclusive)."""
    return randint(1, 100)