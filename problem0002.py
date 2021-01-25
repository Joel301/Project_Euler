
#! python3
# -*- coding: utf-8 -*-

"""
Euler description from https://projecteuler.net/
Problem 0002
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million[4000000], find the sum of the even-valued terms.
"""


def fibonacci(limit=4000000):
    lst = [1,2]
    n1, n2 = 1, 2
    while(n2 < limit):
        n = n1 + n2
        n1 = n2
        n2 = n
        lst.append(n)
    return lst



# main function description
def compute():
    ans = sum(x for x in fibonacci(4000000) if x % 2 == 0)
    return str(ans)


if __name__ == "__main__":
    print(compute())
