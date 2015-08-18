"""

Author: Michael Rinos <mer8503@rit.edu>
Description:
File: Program which given a range finds all prime numbers in that range

"""
from math import sqrt

def main():
	sRange = 2
	eRange = int(input("Enter an end index: "))
	if eRange < 2:
		print("End index must be >= 2")
	else:
		primes = []
		for i in range(2,eRange+1):
			if isPrime(i):
				primes.append(i)
	print(primes)
			

def isPrime(number):
	if number ==2:
		return True
	if number% 2 ==0:
		return False
	for i in range (3,int(sqrt(number))+1,2):
		if number % i == 0:
			return False
	return True

main()
