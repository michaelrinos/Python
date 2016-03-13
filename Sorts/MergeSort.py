def MergeSort(lst):
    if lst == []:
        return lst
    elif len(lst) == 1:
        return (lst)
    else:
        blst = lst[:len(lst)//2]
        clst = lst[len(lst)//2:]
        return MergeList(MergeSort(blst), MergeSort(clst))
def MergeList(alst, blst):
    flst = []
    acount = 0
    bcount = 0
    while acount < len(alst) and bcount < len(blst):
        if alst[acount] <= blst[bcount]:
            flst.append(alst[acount])
            acount= acount + 1
        else:
            flst.append(blst[bcount])
            bcount = bcount + 1
    if acount < len(alst):
        flst.extend(alst[acount:])
    elif bcount < len(blst):
        flst.extend( blst[bcount:])
    return flst



if __name__ == '__main__':
    assert MergeSort([1, 2, 3, 4, 5]) == [1,2,3,4,5], "First"
    assert MergeSort([1, 4, 3, 2, 5]) == [1,2,3,4,5], "Second"
    assert MergeSort([2, 1, 4, 5, 3]) == [1,2,3,4,5], "Third"
    assert MergeSort([5, 4, 3, 2, 1]) == [1,2,3,4,5], "Fourth"