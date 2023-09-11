list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list2 + list1 # The lists sum order matters
list4 = list(range(1, 10, 2)) # Creating a list that goes from number 1 to 10, jumping from 2 to 2.
print(list4); print(list3)

list3 = list1 + list2
print(list3)

list2.extend(list1) # Adds 'list1' to the 'list2' contents
print(list2)

list1.append(4) # Adds an item to the list end
print(list1)

list1.insert(0, 'test') # Inserts the described content into the indicated index. (list[0] -> 'test')
print(list1)

del(list1[3]) # Removes what is contained in the mentioned index.
print(list1)