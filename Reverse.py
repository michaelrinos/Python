"""

Author: Michael Rinos <mer8503@cs.rit.edu>
File: Reverse
Description: Enter a string and the program will reverse it and print it out.

"""

def main():
	string = str(input("Enter a string to reverse: "))
	print(string[::-1])
	input("Press enter to exit")
main()