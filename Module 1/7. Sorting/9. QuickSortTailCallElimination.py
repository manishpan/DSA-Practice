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

def QuickSortTailCallElimination(arr, p, r):
    while p < r:
        q = HoarePartition(arr, p, r)
        QuickSortTailCallElimination(arr, p, q)
        p = q + 1

arr = [8, 4, 7, 9, 3, 10, 59]
QuickSortTailCallElimination(arr, 0, len(arr)-1)
print(arr)