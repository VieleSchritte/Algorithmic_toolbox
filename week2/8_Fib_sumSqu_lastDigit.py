from sys import stdin


def FibSquSum_lastDigit(n):  # 0 1 1 2 3 5 8 13 21 34 55 89
    if n <= 1:
        return n
    previous, current, reminder = 0, 1, n % 60
    if reminder == 0:
        return reminder
    for i in range(2, reminder + 3):
        previous, current = current % 10, (previous + current) ** 2 % 10
    result = current - 1
    if result // 10 == 0:
        return current - 1
    return (current - 1) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(FibSquSum_lastDigit(n))
