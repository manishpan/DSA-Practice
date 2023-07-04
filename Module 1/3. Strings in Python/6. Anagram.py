def Anagram1(s1, s2):
    if len(s1) != len(s2):
        return "No"
    s1_dict = {x : s1.count(x) for x in s1}
    s2_dict = {x : s2.count(x) for x in s2}
    if s1_dict == s2_dict:
        return "Yes"

def Anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    countarr = [0] * 256
    for i in range(len(s1)):
        countarr[ord(s1[i])] = countarr[ord(s1[i])] + 1
        countarr[ord(s2[i])] = countarr[ord(s2[i])] - 1
    for x in countarr:
        if x != 0:
            return False
    return True
    

s1 = "listen"
s2 = "silent"
print(Anagram1(s1, s2))
print(Anagram2(s1, s2))