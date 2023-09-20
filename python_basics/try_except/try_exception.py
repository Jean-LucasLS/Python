a = 10
b = 0

try:
  print('Breakpoint 1')
  c = a / b * h # ZeroDivisionError, NameError
  print(b)
  print('Breakpoint 2')
  print(b[0]) # TypeError
  print('Breakpoint 3'[100]) # IndexError
  
#### Specifing the error ####
 
except ZeroDivisionError as error:
  print('Division by zero.')
  print('Message:', error)
  print('Name:', error.__class__.__name__)
  
except NameError:
  print('Variable not defined.')

# Two possible erros, passed as a 'tuple'
except (TypeError, IndexError) as error:
  print('Type error or IndexError.')
  print('Message:', error)
  print('Name:', error.__class__.__name__)
  
# "Exception"  is triggered when the error was not evidenced in the "expects" above
except Exception:
  print('Unknown error.')