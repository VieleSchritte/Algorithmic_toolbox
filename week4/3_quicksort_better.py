import sys


def quickSort(array, left, right):
    if left >= right:
        return
    mid = partition(array, left, right)
    quickSort(array, left, mid)
    quickSort(array, mid + 1, right)


def partition(array, left, right):
    pivot = array[left]
    j = left
    for i in range(left + 1, right):
        if array[i] <= pivot:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[j], array[left] = array[left], array[j]
    return j


if __name__ == '__main__':
    raw_input = sys.stdin.read()
    array = list(map(int, raw_input.split()))[1:]
    quickSort(array, 0, len(array))
    str_result = ''
    for character in array:
        str_result += str(character) + ' '
    print(str_result)
