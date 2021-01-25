
#! python3
# -*- coding: utf-8 -*-

"""
Euler description from https://projecteuler.net/
Problem 0005

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def is_divisible(number, lstNumbers=range(10)):
    for x in lstNumbers:
        if number % x == 0:
            continue
        return True
    return False


def smallestMultiple(n1=1, n2=10):
    ans = 2
    while is_divisible(ans, list(range(n2, n1-1, -1))):
        ans += 1
    return ans


def orderedArray(n1=1, n2=10):
    # order the numbers

    # main function description
    pass


def compute():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)


if __name__ == "__main__":
    print(smallestMultiple(n1=1, n2=20))
