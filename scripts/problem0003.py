#! python3
#-*- coding: utf-8 -*-

"""
Euler description from https://projecteuler.net/
Problem 0003
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def primeFactors(number= 13195):
	p=2
	while number >= p*p:
		if number % p == 0:
			yield p
			number = number/p
		else:
			p=p+1
	yield int(number)
	return

#main function
def compute():
	ans = [x for x in primeFactors(600851475143)]
	return ans


if __name__ == "__main__":
	print(compute())