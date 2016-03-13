def SelectionSort(lst):
    max = len(lst)
    for i in range(max):
        key = lst[i]
        keyj = i
        for j in range(i+1, max):
            if lst[j] < key:
                key = lst[j]
                keyj = j
        lst[keyj], lst[i] = lst[i], key
    return lst

if __name__ == '__main__':
    assert SelectionSort([1, 2, 3, 4, 5]) == [1,2,3,4,5], "First"
    assert SelectionSort([1, 4, 3, 2, 5]) == [1,2,3,4,5], "Second"
    assert SelectionSort([2, 1, 4, 5, 3]) == [1,2,3,4,5], "Third"
    assert SelectionSort([5, 4, 3, 2, 1]) == [1,2,3,4,5], "Fourth"