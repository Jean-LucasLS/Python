nums     = [1, 2, 3, 4, 5]
new_nums = [num for num in nums]
division = [num / 2 for num in nums]

nums[0] = 800
print(nums, new_nums, division, sep='\n')