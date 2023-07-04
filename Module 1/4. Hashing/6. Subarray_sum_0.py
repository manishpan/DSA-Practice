def isZeroSum(l):
    pre_sum = 0
    h = set()
    for i in l:
        pre_sum = pre_sum + i
        if pre_sum in h:
            return True
        h.add(pre_sum)
    return False

l = [3, 1, -2, 5,6]
print(isZeroSum(l))