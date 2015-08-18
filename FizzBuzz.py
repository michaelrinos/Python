"""

Author: Michael Rinos <mer8503@cs.rit.edu>
File: FizzBuzz
Description: Program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number 
and for the multiples of five print “Buzz”. For numbers which 
are multiples of both three and five print “FizzBuzz”.

"""

def main():
	for i in range(0,int(input("Enter a number to stop at: "))+1):
		if i%3==0 and i%5==0 and i != 0:
			print("FizzBuzz")
		elif i%3==0 and i !=0:
			print("Fizz")
		elif i%5==0 and i !=0:
			print("Buzz")
		else:
			print(i)
	input("Press enter to finish")
main()