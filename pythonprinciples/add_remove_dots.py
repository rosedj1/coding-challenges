"""Add and remove dots from a string.

Author: Dr. Jake Rosenzweig
Date: 2023-11-08

Challenge: 
Difficulty: 3/10
URL: https://pythonprinciples.com/challenges/???

Write a function named add_dots that takes a string and adds "." in between
each letter. For example, calling add_dots("test") should return the string
"t.e.s.t". Then, below the add_dots function, write another function named
remove_dots that removes all dots from a string. For example, calling
remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should
return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)

Performance Testing:
====================
Jake's Solution:
>>> %timeit add_dots(s_test)                                                                 
230 ns ± 1.73 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit remove_dots('t.e.s.t')                                                           
186 ns ± 0.23 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> %timeit remove_dots(add_dots('test'))                                                    
401 ns ± 2.36 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

Example Solution:
>>> %timeit add_dots_eg(s_test)                                                              
434 ns ± 3.48 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit remove_dots_eg('t.e.s.t')                                                        
413 ns ± 1.62 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit remove_dots_eg(add_dots_eg('test'))                                              
837 ns ± 9.57 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
!!! Review lessons!
* 
"""
def add_dots(s):
    """Return a string with a dot between each letter in `s` (string)."""
    return '.'.join(s)

def remove_dots(s):
    """Return a string with all dots removed in `s` (string)."""
    return s.replace('.', '')

s_test = "test"

# Example Solution:
def add_dots_eg(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots_eg(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out

if __name__ == '__main__':
    add_dots(s_test)
    remove_dots('t.e.s.t')
    remove_dots(add_dots('test'))

    add_dots_eg(s_test)
    remove_dots_eg('t.e.s.t')
    remove_dots_eg(add_dots_eg('test'))
    # print(f"Should return 't.e.s.t:' {add_dots(s_test)}")
    # print(f"Should return 'test:' {remove_dots('t.e.s.t')}")
    # print(f"Should return 'test:' {remove_dots(add_dots('test'))}")