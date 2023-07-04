s1 = {10, 20, 30}
print(s1)
print(type(s1))

s2 = set([20, 30, 40])
print(s2)

s3 = {}
print(type(s3))

s4 = set()
print(type(s4))
print(s4)

s = {10, 20}
s.add(30)
print(s)
s.add(30)
print(s)
s.update([40, 50])
print(s)
s.update({60,70}, [80, 90])
print(s)

s = {10,30,20,40}
s.discard(30)
print(s)
s.remove(20)
print(s)
s.clear()
print(s)
s.add(50)
del s

s = {10, 30, 20, 40}
print(len(s))
print(20 in s)
print(50 in s)

s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

s1 = {2,4,6,8}
s2 = {4,8}

print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1 < s2)
print(s1.issuperset(s2))
print(s1 > s2)