"""

Author: Michael Rinos <mer8503@rit.edu>
File: CollatzConjecture.py
Description: Collatz Conjecture in python

"""

def main():
	steps = []
	start = int(input("Enter a number to start at: "))
	steps.append(start)
	while(start > 1):
		if start%2 == 0:
			start = start/2
		else:
			start = start * 3 + 1 
		steps.append(start)
	print("It took "+ str(len(steps)-1) + "steps to get to 1!")
	print(steps)
	input("Press enter to quit")
main()
