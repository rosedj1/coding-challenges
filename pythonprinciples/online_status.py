"""

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

#=======================#
#=== Lessons Learned ===#
#=======================#

! DO PERFORMANCE TESTING !
"""
def online_count(dct):
    return sum([True for val in dct.values() if val == "online"])

# Example Solution 1.
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

# Example Solution 2.
def online_count(people):
    return len([p for p in people if people[p] == "online"])

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

if __name__ == '__main__':
    print(f'''Should return 2: {online_count(statuses)}''')
