s1 = "geeksforgeeks"
s2 = "geeks"
print(s2 in s1)
print(s2 not in s1)


print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2, 1, len(s1)))

s1 = "geeks     for   geeks"
print(s1.split(" "))

s = "-----geeksforgeeks--"
print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))