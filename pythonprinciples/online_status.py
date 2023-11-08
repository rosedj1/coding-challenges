"""Count the number of people who are online.

Author: Dr. Jake Rosenzweig
Date: 2023-10-31, Happy Halloween!

Challenge: Online Status
Difficulty: 2/10
URL: https://pythonprinciples.com/challenges/Online-status/

The aim of this challenge is, given a dictionary of people's online status,
to count the number of people who are online.
For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

In this case, the number of people online is 2.

Write a function named online_count that takes one parameter.
The parameter is a dictionary that maps from strings of names to the string
"online" or "offline", as seen above.

Your function should return the number of people who are online.

Performance Testing:
====================
>>> %timeit online_count(statuses)                                                           
391 ns ± 2.49 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit online_count_generator(statuses)                                                      
421 ns ± 5.17 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit online_count_egsoln1(statuses)                                                   
279 ns ± 0.668 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
>>> %timeit online_count_egsoln2(statuses)                                                   
383 ns ± 1.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* Summing a generator is surprisingly the *slowest*! Was this an exception?
   - Summing a list of bools was faster.
* Fastest soln was a for loop, a counter, and unpacking key, val pairs.
* Can do some performance testing by doing:
   - >>> python -m cProfile myscript.py
   - Include the `-s time` flag to sort by most expensive calls up top.
"""
def online_count(dct):
    return sum([True for val in dct.values() if val == "online"])

def online_count_generator(dct):
    return sum(True for val in dct.values() if val == "online")

# Example Solution 1.
def online_count_egsoln1(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

# Example Solution 2.
def online_count_egsoln2(people):
    return len([p for p in people if people[p] == "online"])

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

if __name__ == '__main__':
    print(f'''Should return 2: {online_count(statuses)}''')
    print(f'''Should return 2: {online_count_generator(statuses)}''')
    print(f'''Should return 2: {online_count_egsoln1(statuses)}''')
    print(f'''Should return 2: {online_count_egsoln2(statuses)}''')
