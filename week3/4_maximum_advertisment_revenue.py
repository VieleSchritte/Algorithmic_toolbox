import sys


def advertisements(profits_per_click, estimated_clicks):
    profits_per_click = sorted(profits_per_click, reverse=True)
    estimated_clicks = sorted(estimated_clicks, reverse=True)
    overall_profit = 0
    for i in range(len(profits_per_click)):
        overall_profit += profits_per_click[i] * estimated_clicks[i]
    return overall_profit


if __name__ == '__main__':
    raw_data = sys.stdin.read()
    data = list(map(int, raw_data.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(advertisements(a, b))
