numbers = list(map(int, input().split()))
number = sorted(numbers)
print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(number[0], number[1], number[2], numbers[0], numbers[1], numbers[2]), end='\n')
