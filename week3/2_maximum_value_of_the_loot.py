import sys


def get_optimal_value(capacity, weights, values):
    overall_price = 0
    while capacity != 0 and len(weights) != 0 and len(values) != 0:
        max_price = index = 0
        for i in range(len(values)):
            if values[i] / weights[i] > max_price:
                max_price = values[i] / weights[i]
                index = i

        V_to_loot = min(capacity, weights[index])
        overall_price += max_price * V_to_loot
        capacity -= V_to_loot
        weights.pop(index)
        values.pop(index)
    return overall_price


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
