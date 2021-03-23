import sys


def Fib_again(n, m):
    previous, current = 0, 1
    period_len = 0

    for i in range(m ** 2):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            period_len = i + 1
    return Fibonacci(n % period_len) % m


def Fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for i in range(2, n + 1):
        previous, current = current, previous + current
    return current


if __name__ == '__main__':
    custom_input = sys.stdin.read()
    n, m = map(int, custom_input.split())
    print(Fib_again(n, m))
