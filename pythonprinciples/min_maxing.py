"""Find the largest difference in a list. 

Author: Dr. Jake Rosenzweig
Date: 2023-11-17, Happy Birthday Carina!

Challenge: Min-maxing
Difficulty: 3/10
URL: https://pythonprinciples.com/challenges/Minmaxing/

Define a function named largest_difference that takes a list of numbers as its
only parameter. Your function should compute and return the difference between
the largest and smallest number in the list. For example, the call
largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2. You may
assume that no numbers are smaller or larger than -100 and 100.

Performance Testing:
====================
>>> %timeit largest_difference(range(1000))                                                               
42.6 µs ± 97.8 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
>>> %timeit largest_difference_egsoln(range(1000))                                                        
69.6 µs ± 385 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

#=======================#
#=== Lessons Learned ===#
#=======================#
* I'm surprised that the "naive solution" below isn't that much slower than
    the short solution. Short solution is only 1.63 times faster!
"""
def largest_difference(ls_num):
    """Return the largest difference between two numbers in `ls_num`."""
    return max(ls_num) - min(ls_num)

# Naive solution
def largest_difference_egsoln(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference

if __name__ == '__main__':
    print(f'''Should be 6: {largest_difference([9, 3, 4, 8, 4])}''')
    print(f'''Should be 2: {largest_difference([1, 2, 3])}''')
