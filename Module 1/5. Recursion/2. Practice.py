def fun(n):
    if n < 1:
        return
    print(n)
    fun(n-1)
    print(n)

fun(7)