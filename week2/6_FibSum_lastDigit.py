import sys


def FibSum_lastDigit(n):
    if n <= 1:
        return n
    previous, current, remainder = 0, 1, n % 60
    if remainder == 0:
        return remainder
    for i in range(2, remainder + 3):
        previous, current = current, (previous + current) % 60
    result = current - 1
    if result // 10 == 0:
        return result
    return result % 10


if __name__ == '__main__':
    custom_input = sys.stdin.read()
    n = int(custom_input)
    print(FibSum_lastDigit(n))
