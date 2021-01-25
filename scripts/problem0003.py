  
#! python3
#-*- coding: utf-8 -*-

"""
Euler description from https://projecteuler.net/
Problem 0003
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def divisibles(number= 13195):
	p=2
	while number >= p*p:
		if number % p == 0:
			print(p,", ")
			number = number/p
		else:
			p=p+1
	print(number)

#main function description
def compute():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)


if __name__ == "__main__":
	#print(compute())
	print(divisibles())
