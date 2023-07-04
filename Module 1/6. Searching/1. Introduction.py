def linearSearch(l, k):
    for i in range(0,len(l)):
        if l[i] == k:
            return i
    return -1

l = [2, 5, 2 , 8, 90, 101, 45, 56]
k = 45

print(linearSearch(l, k))

def BinarySearch(l, k):
    low, high = 0, len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if (l[mid] == k):
            return mid
        elif l[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(sorted(l))
print(BinarySearch(sorted(l), 450))