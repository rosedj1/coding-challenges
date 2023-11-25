"""Count the largest number of consecutive zeros in a string.

Author: Dr. Jake Rosenzweig
Date: 2023-11-25

Challenge: Consecutive zeros
Difficulty: 4/10
URL: https://pythonprinciples.com/challenges/Consecutive-zeros/

The goal of this challenge is to analyze a binary string consisting of only
zeros and ones. Your code should find the biggest number of consecutive zeros
in the string. For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which
is the string of zeros and ones. Your function should return the number
described above.

Performance Testing:
====================
In [1]: %timeit unit_test(consecutive_zeros)
3.3 µs ± 18.2 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [2]: %timeit unit_test(consecutive_zeros_egsoln1)
3.07 µs ± 4.29 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [3]: %timeit unit_test(consecutive_zeros_egsoln2)
2.56 µs ± 13.8 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* There was certainly a pythonic way to solve this challenge!
    And sure enough the pythonic way is the most efficient:
    approx. 29% faster than mine.
"""
# My solution (18 lines):
def consecutive_zeros(chars):
    """Return the largest number of consecutive 0's in the string `chars`."""
    largest_num_zeros = 0
    if chars == '0':
        return 1
    for idx, char in enumerate(chars):
        if char == '0':
            # Zero found. Start counting.
            this_num_zeros = 1
            next_idx = idx + 1
            for next_char in chars[next_idx:]:
                if next_char == '0':
                    this_num_zeros += 1
                else:
                    break
            if this_num_zeros > largest_num_zeros:
                largest_num_zeros = this_num_zeros
    return largest_num_zeros

# Example solution, even shorter than mine (11 lines).
def consecutive_zeros_egsoln1(bin_str):
    """Return the largest number of consecutive 0's in the string `chars`."""
    streak = 0
    result = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(streak, result)
    return result

# Elegant example solution:
def consecutive_zeros_egsoln2(bin_str):
    """Return the largest number of consecutive 0's in the string `chars`."""
    return max(len(s) for s in bin_str.split("1"))

def unit_test(fn):
    """Use with the %timeit magic in iPython. `fn` is a function."""
    fn("0")
    fn("111")
    fn("111000")
    fn("101001")
    fn("00101010")
    fn("100000011")
    fn("0000")

if __name__ == '__main__':
    unit_test(consecutive_zeros)
    unit_test(consecutive_zeros_egsoln1)
    unit_test(consecutive_zeros_egsoln2)
