def Panagram(s):
    s = s.lower()
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s:
        if i in alphabets:
            alphabets.remove(i)
    if len(alphabets) == 0:
        return "The given string is already a panagram."
    return "".join(alphabets)

s1 = "Thequickbrownfoxjumpsoverthelazydog"
s2 = "Abcdefghijklmnopqrstuvwxy"
print(Panagram(s2))