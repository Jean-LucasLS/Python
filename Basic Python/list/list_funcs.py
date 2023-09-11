list = ['Jucaju', 3, 43.3]

del list[2] # Deletes the specified element, causing the elements in front to move their current indexes back by one unit
print(list, end='\n\n')

list.append([111, 'Jockey']) # Adding a list as an element of another list
print(f'{list} | {list[2]} type is {type(list[2])}', end='\n\n')

del_last = list.pop() # Saving the last element removed from the list that was removed by the 'pop' method
print(f'list: {list} | pop: {del_last}', end='\n\n')

list.insert(1, 'Cajuca') # The 'insert' method receives (list_index, element_to_add)
print(list, end='\n\n')

list.insert(50000000, 'DIGNITAS') # If the index exceeds the size of the list, the element will be added after the largest current index
print(f'list: {list} | list[4]: {list[3]} | list[50000000]: IndexError: list index out of range', end='\n\n')

list2 = ['Mojito', 22, 'Totem']
print(f'list + list2 = {list + list2} | list2 + list = {list2 + list}', end='\n\n') # Joining two lists using the '+' operation

list.extend(list2) # The 'extend' function necessarily changes the list that calls the method, and cannot store it in a third variable
print(f'list.extend(list2) = {list}')