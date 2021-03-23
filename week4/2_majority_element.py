import sys


def majority(array):
    array.sort()
    current_elem = array[0]
    current_count = max_count = 1
    for i in range(1, len(array)):
        if current_count > max_count:
            max_count = current_count
        if array[i] == current_elem:
            current_count += 1
        else:
            current_elem, current_count = array[i], 1
    if current_count > max_count:
        max_count = current_count
    if max_count > len(array) // 2:
        return 1
    return 0


if __name__ == '__main__':
    data_input = sys.stdin.read()
    raw_data = list(map(int, data_input.split()))[1:]

    print(majority(raw_data))
