import sys


def GCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return GCD(a % b, b)
    return GCD(b % a, a)


if __name__ == "__main__":
    custom_input = sys.stdin.read()
    a, b = map(int, custom_input.split())
    print(GCD(a, b))
