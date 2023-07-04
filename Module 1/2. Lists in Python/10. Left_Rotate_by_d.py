def Reverse_list(l, s, e):
    while(s < e):
        l[s], l[e] = l[e], l[s]
        s = s + 1
        e = e - 1

def Left_Rotate_by_d(l, d):
    n = len(l)
    if d == 0:
        return l
    elif d > n:
        d = d - n
    Reverse_list(l, 0, d-1)
    Reverse_list(l, d, n-1)
    Reverse_list(l, 0, n-1)

l = [10, 20, 30, 40, 50]
d = 3
Left_Rotate_by_d(l ,d)
print(l)