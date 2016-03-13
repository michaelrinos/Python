def InsertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j = j -1
        lst[j+1] = key
    return lst

if __name__ == '__main__':
    assert InsertionSort([1, 2, 3, 4, 5]) == [1,2,3,4,5], "First"
    assert InsertionSort([1, 4, 3, 2, 5]) == [1,2,3,4,5], "Second"
    assert InsertionSort([2, 1, 4, 5, 3]) == [1,2,3,4,5], "Third"
    assert InsertionSort([5, 4, 3, 2, 1]) == [1,2,3,4,5], "Fourth"