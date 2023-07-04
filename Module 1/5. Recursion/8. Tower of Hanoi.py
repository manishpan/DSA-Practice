def ToH(n, A, B, C):
    if n == 1:
        print("Move 1 from", A, "to", C)
        return
    ToH(n-1, A, C, B)
    print("Move", n, "from", A, "to", C)
    ToH(n-1, B, A, C)

ToH(2, "A", "B", "C")