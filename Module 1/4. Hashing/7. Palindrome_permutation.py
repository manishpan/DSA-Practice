from collections import Counter

def isPalPer(s):
    cnt = Counter(s)
    odd = 0
    for freq in cnt.values():
        if freq % 2 != 0:
            odd = odd + 1
            if odd > 1:
                return False
    return True

def Palindrome_permutation(s):
    d = dict()
    for i in range(0, len(s)):
        if s[i] not in d.keys() or d[s[i]] == 0:
            d[s[i]] = 1
            continue
        if d[s[i]] == 1:
            d[s[i]] = 0
    if sum(d.values()) in (0,1):
        return True
    return False

s = "abccbabb"
print(Palindrome_permutation(s))
print(isPalPer(s))