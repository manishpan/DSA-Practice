def Find_Only_Odd(l):
    n = len(l)
    if n % 2 == 0:
        return None
    dkey = {x : l.count(x) for x in l}
    print(dkey)
    for i in dkey.keys():
        if dkey[i] % 2 != 0:
            return i

def Find_Only_Odd2(l):
    n = len(l)
    if n % 2 == 0:
        return None
    for i in l:
        if l.count(i) % 2 != 0:
            return i
        
def Find_Only_Odd3(l):
    res = 0
    for i in l:
        res = res ^ i
    return res

l = [10, 20, 20, 30, 10]
print(Find_Only_Odd3(l))