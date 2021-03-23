import sys


def Fib_last_digit(n):
    if n <= 1:
        return n
    previous, current, result = 0, 1, 0
    for i in range(2, n + 1):
        result = (previous + current) % 10
        previous, current = current, result
    return result


if __name__ == '__main__':
    custom_input = sys.stdin.read()
    n = int(custom_input)
    print(Fib_last_digit(n))
