import sys


def GCDEfficient(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return GCDEfficient(a % b, b)
    return GCDEfficient(b % a, a)


def LCM(a, b):
    GCD = GCDEfficient(a, b)
    return a * b // GCD


if __name__ == '__main__':
    custom_input = sys.stdin.read()
    a, b = map(int, custom_input.split())
    print(LCM(a, b))
