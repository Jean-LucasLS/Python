l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8, 9, 10, 11, 12]
l3 = [x + y for x, y in zip(l1, l2)]

print(list(zip(l1, l2)))
print(l3)