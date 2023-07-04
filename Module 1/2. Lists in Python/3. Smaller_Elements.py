def getSmallerElements(l, x):
    return [i for i in l if i < x] 

l = [8, 100, 20, 40, 3, 7]
x = 10
output_l = getSmallerElements(l, x)
print(output_l)