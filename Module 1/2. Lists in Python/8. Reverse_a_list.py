def Reverse_list(l):
    s, e = 0, len(l) - 1
    while(s < e):
        l[s], l[e] = l[e], l[s]
        s = s + 1
        e = e - 1
    return l

l1 = [10, 20, 30, 40, 50]
l2 = ["geeks", "ide", "courses"]

print(Reverse_list(l1))
print(Reverse_list(l2))