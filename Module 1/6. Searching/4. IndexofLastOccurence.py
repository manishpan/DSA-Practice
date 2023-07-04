def LastIndex(l, k):
    n = len(l)
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > k:
            high = mid - 1
        elif l[mid] < k:
            low = mid + 1
        else:
            if mid == n-1 or l[mid+1] != l[mid]:
                return mid
            low = mid + 1
    return -1

l = [10, 15, 15, 15, 20]
k = 15
print(LastIndex(l, k))