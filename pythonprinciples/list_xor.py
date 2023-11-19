"""See if a number is exclusively in one list or the other.

Author: Dr. Jake Rosenzweig
Date: 2023-11-18

Challenge: List xor
Difficulty: 5/10
URL: https://pythonprinciples.com/challenges/List-xor/

Define a function named list_xor. Your function should take three parameters:
    n, list1, and list2.
Your function must return whether n is exclusively in list1 or list2.
In other words, if n is in both lists or in none of the lists, return False.
If n is in only one of the lists, return True.

For example:
    list_xor(1, [1, 2, 3], [4, 5, 6]) == True
    list_xor(1, [0, 2, 3], [1, 5, 6]) == True
    list_xor(1, [1, 2, 3], [1, 5, 6]) == False
    list_xor(1, [0, 0, 0], [4, 5, 6]) == False


Performance Testing:
====================
My implementation:
>>> %timeit list_xor(1, range(2,10002), range(10000))                                                     
511 ns ± 2.63 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

Example Solution 1:
>>> %timeit list_xor_egsoln1(1, range(2,10002), range(10000))                                             
479 ns ± 1.23 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

Example Solution 2:
>>> %timeit list_xor_egsoln2(1, range(2,10002), range(10000))                                             
526 ns ± 4.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* The built-in xor operator in this case is approx. 6.7% faster than my soln.
CONCLUSION: It's a neat operator to use and will improve code a little.
"""
def list_xor(num, ls1, ls2):
    """Return True, iff `num` is only in `ls1` or only in `ls2`."""
    return (num in ls1 and num not in ls2) or (num in ls2 and num not in ls1)

# Example Solution 1:
# smart solution: uses the built-in xor operator ^
def list_xor_egsoln1(n, list1, list2):
    return (n in list1) ^ (n in list2)

# Example Solution 2:
# naive solution: check each case at a time
def list_xor_egsoln2(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True

if __name__ == '__main__':
    print(f'''Should be True: {list_xor(1,  [1, 2, 3], [4, 5, 6])}''')
    print(f'''Should be True: {list_xor(1,  [0, 2, 3], [1, 5, 6])}''')
    print(f'''Should be False: {list_xor(1, [1, 2, 3], [1, 5, 6])}''')
    print(f'''Should be False: {list_xor(1, [0, 0, 0], [4, 5, 6])}''')
