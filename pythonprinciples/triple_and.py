"""Check that all three params are True.

Author: Dr. Jake Rosenzweig
Date: 2023-11-15

Challenge: Boolean and
Difficulty: 4/10
URL: https://pythonprinciples.com/challenges/Boolean-and/

Define a function named triple_and that takes three parameters and returns
True only if they are all True and False otherwise.

Performance Testing:
====================
>>> %timeit 

#=======================#
#=== Lessons Learned ===#
#=======================#
* Example solution was almost twice as fast as mine.
    I used `all()` whereas the example solution used `and`s.
CONCLUSION:
* Use built-in bool comparison operations like `and`, `or`.

"""
def triple_and(bool1, bool2, bool3):
    """Return True only if they are all True and False otherwise."""
    return all((bool1, bool2, bool3))

# Example Solution:
def triple_and_egsoln(a, b, c):
    return a and b and c

if __name__ == "__main__":
    print(f'''Should return True: {triple_and(True, True, True)}''')
    print(f'''Should return False: {triple_and(True, True, False)}''')
    print(f'''Should return False: {triple_and(True, False, True)}''')
    print(f'''Should return False: {triple_and(True, False, False)}''')
    print(f'''Should return False: {triple_and(False, True, True)}''')
    print(f'''Should return False: {triple_and(False, True, False)}''')
    print(f'''Should return False: {triple_and(False, False, True)}''')
    print(f'''Should return False: {triple_and(False, False, False)}''')
