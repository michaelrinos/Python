"""

Author: Michael Rinos <mer8503@rit.edu>
Description: Program which given a range finds all prime numbers in that range

"""
from math import sqrt
import sys

def main():
	sRange = 2
	eRange = int(input("Enter a stoping point: "))
	if eRange <= 2:
		print("End index must be > 2")
		sys.exit(0)
	else:

		primes = []

		for i in range(2,eRange+1):
			#Thanks to checkio for teaching me this neat trick
			if all(i%j for j in range(2,i)):
				primes.append(i)
		print(primes)
main()
