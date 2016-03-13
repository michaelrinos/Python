"""

Author: Michael Rinos <mer8503@cs.rit.edu>
File: Palimdrone
Description: Check if Palindrome - Checks if the string entered by the user is a palindrome. 
That is that it reads the same forwards as backwards like “racecar”

"""

def main():
	string = str(input("Enter a potential palindrome: "))
	middle = len(string)//2
	
	if len(string)%2 == 0:
		if string[:middle] == string[:middle-1:-1]:
			print(string + " is a palindrome")
		else:
			print(string + " isn't a palindrome")
	else:
		if string[:middle] == string[:middle:-1]:
			print(string + " is a palindrome")
		else:
			print(string + " isn't a palindrome")
main()
