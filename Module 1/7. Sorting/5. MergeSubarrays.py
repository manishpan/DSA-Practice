def Merge(A, low, mid, high):
    left, right = A[low:mid+1], A[mid+1:high+1]
    i, j = 0, 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i = i + 1
        else:
            A[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        A[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        A[k] = right[j]
        j = j + 1
        k = k + 1

def MergeSort(A, l, r):
    if l < r:
        m = (l + r) // 2
        MergeSort(A, l, m)
        MergeSort(A, m+1, r)
        Merge(A, l, m, r)

l = [23, 1, 0, 39, 46, 22]
MergeSort(l, 0, len(l)-1)

print(l)