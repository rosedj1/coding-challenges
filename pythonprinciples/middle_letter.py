"""Return the middle letter in a given word or return the empty string.

Author: Dr. Jake Rosenzweig
Date: 2023-10-29

Challenge: Middle Letter
Difficulty: 2/10
URL: https://pythonprinciples.com/challenges/Middle-letter/

Write a function named `mid` that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".

#=======================#
#=== Lessons Learned ===#
#=======================#
* The floor division operator is `//` and it rounds down (hence, 'floor').
"""
# Solution 1.
def mid_soln1(word):
    """Return the middle letter in `word`. If none, return empty string."""
    length = len(word)
    if length % 2 == 0:
        return ''
    else:
        # There is a middle letter.
        idx = length // 2
        return word[idx]

# Solution 2: Combines Solution 1 into single return statement.
# This is essentially what the example solution gave!
def mid_soln2(word):
    """Return the middle letter in `word`. If none, return empty string."""
    length = len(word)
    return '' if length % 2 == 0 else word[length // 2]

if __name__ == '__main__':
    print(f"""Should return 'b': {mid_soln2("abc")}""")
    print(f"""Should return '': {mid_soln2("aaaa")}""")
    print(f"""Should return 't': {mid_soln2("testing")}""")
