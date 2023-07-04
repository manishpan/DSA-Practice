def fun(n):
    if n <= 1:
        return 0
    return 1 + fun(n/2)

x = fun(5)

print(x)