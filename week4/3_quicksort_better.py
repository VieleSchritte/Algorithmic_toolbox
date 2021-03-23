import sys


def sorting(array):
    array_set = set(array)
    result = []
    array_set = list(array_set)
    array_set.sort()
    for character in array_set:
        for i in range(array.count(character)):
            result.append(character)
    return result


if __name__ == '__main__':
    raw_input = sys.stdin.read()
    array = list(map(int, raw_input.split()))[1:]
    result = sorting(array)
    result_str = ''
    for character in result:
        result_str += str(character) + ' '
    print(result_str)
