"""

Author: Michael Rinos <mer8503@rit.edu>
File:MergeSelect
Description:

"""

inversions = 0

def main():
	pass

def mergeSort(aList):
	if aList == []:
		return []
	elif len(aList) == 1:
		return (aList)
	else:
		bList = aList[:len(aList)//2]
		cList = aList[len(aList)//2:]
		return mergeList(mergeSort(bList), mergeSort(cList))

def mergeList(aList, bList):
        
	fList = []
	aCount = 0
	bCount = 0
	while aCount < len(aList) and bCount < len(bList):
		if aList[aCount] <= bList[bCount]:
			fList.append(aList[aCount])
			aCount= aCount + 1
		else:
			fList.append(bList[bCount])
			bCount = bCount + 1
			global inversions
			inversions += len(aList)
	if aCount < len(aList):
		fList.extend(aList[aCount:])
	elif bCount < len(bList):
		fList.extend( bList[bCount:])
	return fList


lst1 = [1, 5, 3, 4, 2, 2, 7, 5, 3, 4, 9, 0, 1, 2, 5, 4, 76, 6]
lst2 = [5, 4, 3, 2, 1]
print(lst2)
print( mergeSort( lst2) )
print(inversions)
