numbers   = [[num, num ** 2] for num in range(10)]
flat_nums = [y for x in numbers for y in x]
print(numbers, flat_nums, sep='\n')