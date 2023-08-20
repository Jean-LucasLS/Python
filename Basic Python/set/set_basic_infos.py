'''Sets can be efficients to remove duplicate values of iterables;
don't have indexes; don't accept imutable values; don't guarantee
ordering; and are iterables (for, in, no in)'''

set1 = set('Jucaju')
set2 = {'Jucaju', 1, 2, 2, 3, 3, 3, 'Jucaju'} # Set removes duplicate values

print(set1, type(set1))
print(set2, type(set2), end='\n\n')

# Tuples can be used in this conext (inside a unic list), because they are IMUTABLE. Lists can't be used
list1 = [1, 2, 2, 3, 3, 3, (1, 2, 3, 3), (1, 2, 3, 3)] 
set3  = set(list1)
list2 = list(set3)

print(list1)
print(set3, type(set3))
print(list2)

print(3 in set3, 4 in set3, 3 not in set3, 4 not in set3) # Testing if a value exists in a specific Set