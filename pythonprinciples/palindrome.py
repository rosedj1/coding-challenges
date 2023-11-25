"""Check if a given string is a palindrome.

Author: Dr. Jake Rosenzweig
Date: 2023-11-25

Challenge: Palindrome
Difficulty: 4/10
URL: https://pythonprinciples.com/challenges/Palindrome/

A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba".
But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter.
Your function should return True if the string is a palindrome,
and False otherwise.

Performance Testing:
====================
In [1]: %timeit palindrome("abcdedcba")
68.5 ns ± 0.329 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [2]: %timeit palindrome_verbose("abcdedcba")
431 ns ± 2.33 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [3]: %timeit palindrome_recursive("abcdedcba")
187 ns ± 0.553 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* Using Python's native reverse-string slice notation is way fast!
"""
# My solution:
def palindrome(word):
    """Return True if `word` is a palindrome."""
    return word == word[::-1]

# iterative solution:
# keep chopping off the head and tail of the string,
# and compare the two. If they are not equal, it's
# not a palindrome. Stop when the string gets too short.
def palindrome_verbose(string):
    while len(string) > 1:
        head = string[0]
        tail = string[-1]
        string = string[1:-1]
        if head != tail:
            return False
    return True

# recursive solution: equivalent to the above.
def palindrome_recursive(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and palindrome(string[1:-1])
# Up to this point, recursion has always baffled me.
# I think I'm finally starting to get it but it's still not intuitive.

if __name__ == "__main__":
    palindrome("bob")