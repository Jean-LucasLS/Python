print(list(range(10)))

list = []
for num in range(10):
  list.append(num)
print(list)

comp_list1 = [num for num in range(10)]
print(comp_list1)

comp_list2 = [num * 2 for num in range(10)]
print(comp_list2)