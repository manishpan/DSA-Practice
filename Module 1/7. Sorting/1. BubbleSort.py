l = [2, 4, 3, 81]

def BubbleSort(l):
    n = len(l)
    for i in range(n-1):
        swapped = False
        for j in range(n - 1- i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if swapped == False:
            break

BubbleSort(l)
print(l)