def binarySearch(lst,start,end,target):
    if start > end:
        return False
    midIndex = (end + start) // 2
    if lst[midIndex] == target:return True
    elif target > lst[midIndex]:
        start = midIndex + 1
        return binarySearch(lst,start,end,target)
    else:
        end = midIndex - 1
        return binarySearch(lst,start,end,target)
