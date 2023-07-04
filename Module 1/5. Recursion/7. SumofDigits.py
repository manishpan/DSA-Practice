def SumofDigits(n):
    if n < 10:
        return n
    return (n % 10) + SumofDigits(n // 10)

print(SumofDigits(984))