def BubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

if __name__ == '__main__':
    assert BubbleSort([1, 2, 3, 4, 5]) == [1,2,3,4,5], "First"
    assert BubbleSort([1, 4, 3, 2, 5]) == [1,2,3,4,5], "Second"
    assert BubbleSort([2, 1, 4, 5, 3]) == [1,2,3,4,5], "Third"
    assert BubbleSort([5, 4, 3, 2, 1]) == [1,2,3,4,5], "Fourth"
