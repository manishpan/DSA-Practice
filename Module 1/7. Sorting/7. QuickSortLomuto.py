def LomutoPartition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i + 1

def QuickSortLomuto(arr, p, r):
    if p < r:
        q = LomutoPartition(arr, p, r)
        QuickSortLomuto(arr, p, q-1)
        QuickSortLomuto(arr, q+1, r)

arr = [5, 3, 8, 4, 2, 7, 1, 10]
QuickSortLomuto(arr, 0, len(arr)-2)
print(arr)