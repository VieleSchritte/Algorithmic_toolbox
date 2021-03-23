from random import randint


def pairwise(array):
    result = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] * array[j] > result:
                result = array[i] * array[j]
                
    return result


def pairwiseFast(array):
    cases = [0, 1]
    for case in cases:
        if len(array) == case:
            return 0, 0, 0

    max_index1 = max_index2 = 0
    for i in range(len(array)):
        if array[i] > array[max_index1]:
            max_index1 = i

    if max_index1 == 0:
        max_index2 = 1
        for j in range(1, len(array)):
            if array[j] > array[max_index2]:
                max_index2 = j
        return array[max_index1] * array[max_index2], max_index1, max_index2

    for j in range(len(array)):
        if j != max_index1 and array[j] > array[max_index2]:
            max_index2 = j
    return array[max_index1] * array[max_index2], max_index1, max_index2


while True:
    n = randint(0, 3)
    numbers = []
    while n != 0:
        numbers.append(n)
        n -= 1
    result1 = pairwise(numbers)
    result2, max1, max2 = pairwiseFast(numbers)
    if result1 == result2:
        print('OK')
    else:
        print('Wrong answer, result1 =', result1, ', result2 =', result2, ', max1 =', max1, ', max2 =', max2)
        print(numbers)
        break
