#Naive Partiton
def NaivePartition(arr, p):
    n = len(arr)
    arr[p], arr[n-1] = arr[n-1], arr[p]
    temp = []

    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)

    for x in arr:
        if x > arr[n-1]:
            temp.append(x)

    for i in range(n):
        arr[i] = temp[i]

#Lomuto Partition
def LomutoPartition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i + 1

#Hoare Partition
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