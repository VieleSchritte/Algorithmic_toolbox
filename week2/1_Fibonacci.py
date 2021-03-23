def Fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for i in range(2, n + 1):
        previous, current = current, previous + current
    return current


n = int(input())
print(Fibonacci(n))
