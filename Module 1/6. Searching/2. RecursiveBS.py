def RecursiveBS(l, k, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if l[mid] == k:
        return mid
    elif l[mid] > k:
        return RecursiveBS(l, k, low, mid-1)
    else:
        return RecursiveBS(l, k, mid+1, high)
    
def RecursiveBSMain(l, k):
    return RecursiveBS(l, k, 0, len(l) - 1)

l = [10, 20, 30, 40, 50, 60]
k = 40
print(RecursiveBSMain(l, k))