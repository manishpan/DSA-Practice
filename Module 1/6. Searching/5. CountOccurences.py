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

def CountOccurences(l, k):
    fi = FirstIndex(l, k)
    if fi == -1:
        return 0
    return LastIndex(l, k) - fi + 1

l = [8, 10, 15,15,15, 20 ,34]
k = 10
print(CountOccurences(l, k))