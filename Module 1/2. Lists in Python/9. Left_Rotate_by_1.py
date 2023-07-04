def Left_Rotate_1(l):
    n = len(l)
    tmp = l[0]
    for i in range(0, n-1):
        l[i] = l[i+1]
    l[n-1] = tmp
    return l

l1 = [10, 20 ,30, 40]
l2 = [1, 2, 3]

print(Left_Rotate_1(l1))
print(Left_Rotate_1(l2))