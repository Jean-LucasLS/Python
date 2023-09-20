# Modules are 'singletons', they can be called once, improving Python efficiency
import def_module
import modularization2.var_module as var_module
import code_module

def_module.test_main()
print(var_module.var5)

# The 'code_module' will not be executed here, because it was executed at the time it was imported
for i in range(3):
  code_module

# In this case, 'code_module' will be executed again, because it was solicitated by 'importlib.reload()'
import importlib
for i in range(3):
  importlib.reload(code_module)

# Reveal all paths beeing used to execute this Python file (as a list)
import sys
print(sys.path[0]) # The first index is the path where this file is

# If '*' is used to import and the module specifies __all__, it will only import the content on '__all__ = [content]'
from modularization2.def_module2 import *
print(var1)

# The function 'sum_num' and 'var2' were imported because they were specificed ('*' would not reach them)
from modularization2.def_module2 import sum_num, var2
print(var2)
sum_num(1, 2)
