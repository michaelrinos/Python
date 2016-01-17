
"""

Author: Michael Rinos <mer8503@cs.rit.edu>
File: Count Vowels
Description:  Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.

"""

def main():
	a,e,i,o,u = ( 0 for i in range(6))
	vowels = [a,e,i,o,u]
	
	string = str(input("Enter a string to find its vowels"))

def head(string):
	return string[0]

def tail(string):
	return string[1:]

def check(string, count, vowels):
	if head(string) not in vowels:
		check(tail(string),count,vowels)
	elif 
	