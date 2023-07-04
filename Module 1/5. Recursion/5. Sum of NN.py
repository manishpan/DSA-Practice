def SumNN(n):
    if n == 1:
        return 1
    return n + SumNN(n - 1)

print(SumNN(5))

n = int(input("Enter n: "))
sum = n * (n+1) // 2
print("Sum :", sum)