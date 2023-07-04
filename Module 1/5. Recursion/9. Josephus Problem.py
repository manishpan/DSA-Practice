def JosephusProblem(n, k):
    if n == 1:
        return 0
    return (JosephusProblem(n-1, k) + k) % n


print(JosephusProblem(5, 3))