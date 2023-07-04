def Second_Largest_Element(s):    
    if len(s) < 2:
        return None
    
    lar = s[0]
    slar = None

    for x in s[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar
 

l = [10, 10, 10, 3]
print(Second_Largest_Element(l))