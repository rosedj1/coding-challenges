"""<Brief description>

Author: Dr. Jake Rosenzweig
Date: 2023-11-13, Happy birthday to mea discipula Helena!

Challenge: Writing short code
Difficulty: 5/10
URL: https://pythonprinciples.com/challenges/Writing-short-code/

Define a function named `convert` that takes a list of numbers as its only
parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a single
line of code.

Performance Testing:
====================
>>> %timeit convert([num for num in range(10)])                                                                
2.06 µs ± 33.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# Using `map` is just a little faster.
>>> %timeit convert_egsoln([num for num in range(10)])                                                         
1.71 µs ± 11.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* The `map` function may be only slightly faster than a typical list
    comprehension. However, if `map` and lambda function are used together,
    they can be even slower than list comprehensions.
    Conclusion: use list comprehensions.
"""
def convert(ls_nums):
    """Return a list of strings, converting each number into a string."""
    return [str(num) for num in ls_nums]

# Example Solution using `map`:
def convert_egsoln(ns):
    """Return a list of strings, converting each number into a string."""
    return list(map(str, ns))

if __name__ == '__main__':
    print(convert([1, 2, 3]))