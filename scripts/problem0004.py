
#! python3
# -*- coding: utf-8 -*-

"""
Euler description from https://projecteuler.net/
Problem 0004
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largestPalindrome(digits=2):
    start = int('1'.ljust(digits, '0'))
    n1, n2 = start, start
    ans = 0
    while n1 <= start*10:
        while n2 <= start*10:
            if str(n1*n2) == str(n1*n2)[::-1]:
                if ans < n1*n2:
                    ans = n1*n2
            n2 += 1
        n1 += 1
        n2 = n1
    return ans

if __name__ == "__main__":
    print(largestPalindrome(3))
