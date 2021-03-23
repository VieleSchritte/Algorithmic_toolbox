import sys


def FibSum_lastDigit(n):  # 0 1 1 2 3 5 8 13 21 34 55 89
    if n <= 1:
        return n
    previous, current, reminder = 0, 1, n % 60
    if reminder == 0:
        return reminder
    for i in range(2, reminder + 3):
        previous, current = current, (previous + current) % 60
    result = current - 1
    if result // 10 == 0:
        return current - 1
    return (current - 1) % 10


def Fib_partSum_lastDigit(m, n):
    if m == 0 == n:
        return m
    if m == 0:
        return FibSum_lastDigit(n)

    last_n = FibSum_lastDigit(n)
    last_m = FibSum_lastDigit(m - 1)
    if last_m >= last_n:
        return 10 + last_n - last_m
    return last_n - last_m


if __name__ == '__main__':
    custom_input = sys.stdin.read()
    from_, to = map(int, custom_input.split())
    print(Fib_partSum_lastDigit(from_, to))
