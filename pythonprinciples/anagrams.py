"""See if two strings are exact anagrams of each other.

Author: Dr. Jake Rosenzweig
Date: 2023-11-27

Challenge: Anagrams
Difficulty: 3/10
URL: https://pythonprinciples.com/challenges/Anagrams/

Two strings are anagrams if you can make one from the other by rearranging the
letters. Write a function named is_anagram that takes two strings as its
parameters. Your function should return True if the strings are anagrams, and
False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True
while the call is_anagram("Alice", "Bob") should return False.

Performance Testing:
====================
In [1]: %timeit is_anagram("typhoon", "opython")
905 ns ± 3.22 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [2]: %timeit is_anagram_egsoln1("typhoon", "opython")
375 ns ± 7.99 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [3]: %timeit is_anagram_egsoln2("typhoon", "opython")
1.48 µs ± 1.56 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* The example solution used the sorted() function -- an efficient built-in!
    This is a clever solution because it mangles both words.
    This solution is 2.4x faster than my solution.
* My solution is 1.6x faster than the solution which calls 2 functions.
"""
def is_anagram(word1, word2):
    """Return True if `word1` is exactly an anagram of `word2`."""
    # The words can only be anagrams if they are the same length.
    if len(word1) != len(word2):
        return False
    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            return False
    return True

# Example solution 1 (easy):
def is_anagram_egsoln1(string1, string2):
    return sorted(string1) == sorted(string2)

# Example solution 2 (harder):
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram_egsoln2(string1, string2):
    return count_letters(string1) == count_letters(string2)

if __name__ == '__main__':
    print(f"""Should be True: {is_anagram("typhoon", "opython")}""")
    print(f"""Should be False: {is_anagram("Alice", "Bob")}""")
    