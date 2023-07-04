def Separate_Even_Odd(l):
    return [i for i in l if i % 2 == 0], [i for i in l if i % 2 != 0]

l = [10, 41, 30, 15, 80]
even_l, odd_l = Separate_Even_Odd(l)
print(even_l)
print(odd_l)


l1 = [101, 103, 102]
l2 = ["gfg", "ide", "courses"]
d3 = dict(zip(l1, l2))
print(d3.values())

d2 = { v:k for (k,v) in d3.items() }
print(d2)