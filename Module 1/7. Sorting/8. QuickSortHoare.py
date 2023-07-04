def HoarePartition(arr, p, r):
    pivot = arr[p]
    i, j = p-1, r+1
    while True:
        i = i + 1
        while arr[i] < pivot:
            i = i + 1

        j = j - 1
        while arr[j] > pivot:
            j = j - 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def QuickSortHoare(arr, p, r):
    if p < r:
        q = HoarePartition(arr, p, r)
        QuickSortHoare(arr, p, q)
        QuickSortHoare(arr, p+1, r)

arr = [8, 4, 7, 9, 3, 10, 5]
QuickSortHoare(arr, 0, len(arr)-1)
print(arr)