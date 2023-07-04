l = [30, 60, 40]

def average1(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum/len(l)

print(average1(l))

def average2(l):
    return sum(l)/len(l)

print(average2(l))