"""

Author: Michael Rinos <mer8503@cs.rit.edu>
File: Palimdrone
Description: Check if Palindrome - Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”

"""

def main():
	string = str(input("Enter a string to reverse: "))
	print(string==string[::-1])
	
main()
