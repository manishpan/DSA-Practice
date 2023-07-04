def FirstIndex(l, k):
    low, high = 0, len(l)-1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > k:
            high = mid - 1
        elif l[mid] < k:
            low = mid + 1
        else:
            if mid == 0 or l[mid-1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1    

l = [10, 15, 15, 15, 20]
k = 13
print(FirstIndex(l, k))