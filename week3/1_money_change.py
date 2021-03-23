import sys


def money_change(amount):
    coins = 0
    denominations = [1, 5, 10]
    while amount != 0:
        coins += amount // denominations[-1]
        amount = amount % denominations[-1]
        denominations.pop(-1)
    return coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(money_change(m))
