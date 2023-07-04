def Palindrome(txt):
    s, e = 0, len(txt) - 1
    res = "Yes"
    while s < e:
        if txt[s] != txt[e]:
            res = "No"
            break
        s = s + 1
        e = e - 1
    return res

txt = "abnnd"
print(Palindrome(txt))

if txt == txt[::-1]:
    print("Yes")
else:
    print("No")