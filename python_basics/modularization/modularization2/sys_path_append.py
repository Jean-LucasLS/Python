# Using 'sys' function to add the path to the folder containing the desired module
import sys

# Both paths can acess the same folder (1 -> relative path | 2 -> standard computer path)
PATH1 = './modularization'
PATH2 = 'C:\\Users\\jeanl\\OneDrive\\Programação\\Python\\Basic Python\\modularization'

sys.path.append(PATH1) # or (PATH2)

print(sys.path)

# Using a module contained in a folder above this one
import def_module

def_module.test_main()