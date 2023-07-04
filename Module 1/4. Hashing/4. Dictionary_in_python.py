d = {110: "abc", 101: "xyz", 105: "pqr"}
print(d)

d = {}
d["laptop"] = 40000
d["mobile"] = 15000
d["earphone"] = 1000
print(d)
print(d["laptop"])

d = {110: "abc", 101: "xyz", 105: "pqr", 106: "bcd"}
print(d.get(101))
print(d.get(125))
print(d.get(125, "Key not present"))

d[101] = "wxy"
print(len(d))
print(d)
print(d.pop(105))
print(d)
del d[106]
print(d)
d[108] = "cde"
print(d.popitem())