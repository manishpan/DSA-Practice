def Pattern_Searching(txt, pat):
    pos = txt.find(pat)
    while pos >= 0:
        print(pos)
        pos = txt.find(pat, pos + 1)

txt = "geeks for geeks"
pat = "geeks"
Pattern_Searching(txt, pat)