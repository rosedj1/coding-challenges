"""Identify the indices of capital letters in a string.

Author: Dr. Jake Rosenzweig
Date: 2023-10-28

Challenge: Capital Indexes
Difficulty: 2/10
URL: https://pythonprinciples.com/challenges/Capital-indexes/

Write a function named capital_indexes.
The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

#=======================#
#=== Lessons Learned ===#
#=======================#
* List comprehensions are sleek.
* The string module:
    * string.ascii_uppercase ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    * string.ascii_lowercase
* String methods:
    * mystr.isupper()
    * mystr.islower()
"""
import string
# Solution 1 (7 lines, confusing).
def capital_indexes_soln1(mystr):
    ls_idcs = []
    all_upper = mystr.upper()
    for idx, (upper, orig) in enumerate(zip(all_upper, mystr)):
        if upper == orig:
            ls_idcs.extend([idx])
    return ls_idcs

# Solution 2. Cleaner than Solution 1 (6 lines, clean).
def capital_indexes_soln2(mystr):
    ls_idcs = []
    for idx, letter in enumerate(mystr):
        if letter in string.ascii_uppercase:
            ls_idcs.extend([idx])
    return ls_idcs

# Solution 3 (found online, 2 lines, super clean!).
def capital_indexes_soln3(mystr):
    return [idx for idx in range(len(mystr)) if mystr[idx].isupper()]

if __name__ == '__main__':
    print(capital_indexes_soln3("HeLLOjjjjhH"))