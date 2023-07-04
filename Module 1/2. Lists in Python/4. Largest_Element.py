def largest_element(l):
    if not l:
        return None    
    curr_max = l[0]
    for i in range(1, len(l)):
        if curr_max < l[i]:
            curr_max = l[i]
    return curr_max

l = [10, 8, 4, 1]
print(largest_element(l))
print(max(l))