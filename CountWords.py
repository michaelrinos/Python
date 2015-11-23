"""

Author: Michael Rinos <mer8503@cs.rit.edu>
File: CountWords
Description: Enter a text file/text file path and the program will count and
    output the amount of times each word occured

"""
from operator import itemgetter
import re
def main():
    map = ReadFile()
    unsorted_list_of_tups = sorted(map.items(), key=lambda x:x[1])
    unsorted_list_of_tups.sort(key = itemgetter(1))
    #unsorted_list_of_tups.sort(key = itemgetter(1), reverse=True)
    print(unsorted_list_of_tups)






def ReadFile():
    map = {}
    for line in open(input("Enter File Name: ")):
        line =re.split(' ; | , | \* | \n |\s',line)
        for word in line:
            if word in map:
                map[word]+=1
            else:
                map[word]=1
    return map

main()
