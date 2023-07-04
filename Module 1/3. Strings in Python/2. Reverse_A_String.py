def Reverse_String(s):
    n = len(s)
    res = ""
    for i in range(0, n):
        res = s[i] + res
    return res

s = 'geeks'
print(Reverse_String(s))

print(s[::-1])