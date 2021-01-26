#! python3
#-*- coding: utf-8 -*-

"""
Euler description from https://projecteuler.net/
Problem ####
[Description]
"""

#main function description
def compute():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)


if __name__ == "__main__":
	print(compute())