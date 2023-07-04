def list_sorted(l):
    i = 1

    while i < len(l):
        if l[i-1] > l[i]:
            return False
        i = i + 1
    return True

l = []
print(list_sorted(l))