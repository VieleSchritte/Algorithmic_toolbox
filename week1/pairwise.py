def max_fast(numbers):
	if len(numbers) == 0 or len(numbers) == 1:
		return 0
	max1 = max(numbers)
	numbers.remove(max1)
	max2 = max(numbers)
	return max1 * max2


if __name__ == '__main__':
	input_n = int(input())
	input_numbers = [int(x) for x in input().split()]
	print(max_fast(input_numbers))
