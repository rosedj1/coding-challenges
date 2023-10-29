"""Identify consecutive identical letters in a string.

Author: Dr. Jake Rosenzweig
Date: 2023-10-29

Challenge: Double Letters
Difficulty: 3/10
URL: https://pythonprinciples.com/challenges/Double-letters/

The goal of this challenge is to analyze a string to check if it contains two
of the same letter in a row. For example, the string "hello" has l twice in a
row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter.
The parameter is a string. Your function must return True if there are two
identical letters in a row in the string, and False otherwise.

#=======================#
#=== Lessons Learned ===#
#=======================#
To boost performance, exit out of a function ASAP.
See the performance testing below using %timeit magic:

# Test 1: Using a short string with two consecutive identical letters.
>>> %timeit double_letters_jake("hello")
470 ns ± 2.24 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit double_letters_example("hello")
702 ns ± 5.46 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
CONCLUSION: Jake's function finishes 49% faster than example solution.

=====

# Test 2: Using a longer string without consecutive identical letters.
>>> %timeit double_letters_jake("a;fjcidksla;eitugh")
1.07 µs ± 6.24 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit double_letters_example("a;fjcidksla;eitugh")
1.49 µs ± 1.25 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
CONCLUSION: Jake's function finishes 39% faster than example solution.
"""
def double_letters_jake(word):
    """Return True if `word` contains two of the same letter in a row."""
    for first, second in zip(word[:-1], word[1:]):
        if first == second:
            # Exiting here is fast!
            return True
    return False

def double_letters_example(word):
    """Return True if `word` contains two of the same letter in a row."""
    return any(a == b for a, b in zip(word[:-1], word[1:]))

if __name__ == '__main__':
    print(f'''Should return True: {double_letters_jake("hello")}''')
    print(f'''Should return False: {double_letters_jake("nono")}''')
