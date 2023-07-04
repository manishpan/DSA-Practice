def MergeLists(A, B):
    res = []
    m, n = len(A), len(B)
    i, j = 0, 0

    while i < m and j < n:
        if A[i] < B[j]:
            res.append(A[i])
            i = i + 1
        else:
            res.append(B[j])
            j = j + 1
    
    while i < m:
        res.append(A[i])
        i = i + 1

    while j < n:
        res.append(B[j])
        j = j + 1
    
    return res