def Count_Distinct(l):
    return len(set(l))

l1 = [10, 20, 10, 30, 30, 20]
print(Count_Distinct(l1))

l2 = [10, 10, 10]
print(Count_Distinct(l2))

l3 = [10, 20, 30]
print(Count_Distinct(l3))

l4 = []
print(Count_Distinct(l4))

l5 = [10]
print(Count_Distinct(l5))