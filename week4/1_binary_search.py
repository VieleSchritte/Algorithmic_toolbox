# Uses python3
import sys


def Binary_search(search_list, low_index, high_index, key):
    if high_index < low_index:
        return -1
    if key > search_list[-1]:
        return -1
    mid = low_index + (high_index - low_index) // 2
    if key == search_list[mid]:
        return mid
    elif key < search_list[mid]:
        return Binary_search(search_list, low_index, mid - 1, key)
    else:
        return Binary_search(search_list, mid + 1, high_index, key)


def extBinary(high_index, search_list, key_list):
    output = []
    for key in key_list:
        output.append(Binary_search(search_list, 0, high_index, key))
    return output


if __name__ == '__main__':
    data_input = sys.stdin.read()
    data = list(map(int, data_input.split()))
    high = data[0]
    search_list = data[1:high + 1]
    key_list = data[high + 2:]
    output = extBinary(high, search_list, key_list)
    out_string = ''
    for key in output:
        out_string += str(key) + ' '
    print(out_string)
