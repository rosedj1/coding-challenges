"""An interesting challenge! Validate a function definition.

Author: Dr. Jake Rosenzweig
Date: 2023-11-22

Challenge: Solution validation
Difficulty: 5/10
URL: https://pythonprinciples.com/challenges/Solution-validation/

The aim of this challenge is to write code that can analyze code submissions.
We'll simplify things a lot to not make this too hard.

Write a function named `validate` that takes code represented as a string as
its only parameter.

Your function should check a few things:

    the code must contain the def keyword
        otherwise return "missing def"
    the code must contain the `:` symbol
        otherwise return "missing :"
    the code must contain `(` and `)` for the parameter list
        otherwise return "missing paren"
    the code must not contain `()`
        otherwise return "missing param"
    the code must contain four spaces for indentation
        otherwise return "missing indent"
    the code must contain `validate`
        otherwise return "wrong name"
    the code must contain a return statement
        otherwise return "missing return"

If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.

Performance Testing:
====================
# Testing how the solutions evaluate my function.
In [3]: %timeit validate(inspect.getsource(validate))
66.7 µs ± 359 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [4]: %timeit validate_egsoln(inspect.getsource(validate))
65.7 µs ± 159 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

# Testing how the solutions evaluate the solution function.
In [5]: %timeit validate(inspect.getsource(validate_egsoln))
132 µs ± 243 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [6]: %timeit validate_egsoln(inspect.getsource(validate_egsoln))
130 µs ± 129 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* Using the `inspect` module allows us to view a function as a string.
* Basically no performance difference between:
    (1) explicitly laying out all cases, and
    (2) using a for loop + dict.
* However, it took _twice as long_ to `inspect` the example solution because
    it was more verbose (16 lines) vs. my concise function (7 lines).
"""
dct_errs = {
    "def": "missing def",
    ":": "missing :",
    "(": "missing paren",
    ")": "missing paren",
    "    ": "missing indent",
    "validate": "wrong name",
    "return": "missing return"
}

def validate(str_code):
    for word in dct_errs:
        if word not in str_code:
            return dct_errs[word]
    if "(" + ")" in str_code:
        return "missing param"
    return True

# Example Solution:
def validate_egsoln(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True

if __name__ == "__main__":
    import inspect
    validate(inspect.getsource(validate))
