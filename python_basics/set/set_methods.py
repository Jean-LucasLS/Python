s1 = set() # Declares a variable as a 'set'
print(f'set     -> {s1} {type(s1)}')

s1.add('Jucaju'); s1.add(1); s1.add(2) # Add one value to the set
print(f'add     -> {s1} {type(s1)}')

s1.update(('Hello world', 3, 4)) # Adds the passed values
print(f'update  -> {s1} {type(s1)}')

s1.discard('Hello world') # Discard a specific values
print(f'discard -> {s1} {type(s1)}')

s1.clear() # Clear all values in the set
print(f'clear   -> {s1} {type(s1)}')