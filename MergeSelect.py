"""

Author: Michael Rinos <mer8503@rit.edu>
File:MergeSelect
Description:

"""

def main():
	pass
def SelectionSort(list1):
	#sorts the list
	length=len(list1)-1
	x=0
	for j in range (length,-1,-1):
		minval=j
		for i in range(j-1,-1,-1):
			if list1[i]>list1[minval]:
				minval=i
		if minval!=j:
			swap(list1,minval,j)
	return list1

def swap(list1, val1, val2):
	temp = list1[val1]
	list1[val1]=list1[val2]
	list1[val2]=temp

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
	if aCount < len(aList):
		fList.extend(aList[aCount:])
	elif bCount < len(bList):
		fList.extend( bList[bCount:])
	return fList

def MergeSelect(lst, limit):
	if len(lst) == 0:
		return list()
	elif limit > 0:
		return 
	else:
		return mergeSort(lst)


print( mergeSort( [1, 5, 3, 4, 2, 2, 7, 5, 3, 4, 9, 0, 1, 2, 5, 4, 76, 6] ) )
