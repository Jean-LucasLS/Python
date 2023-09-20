# finally will be executed even when 'try' detected an error
try:
  print('Oregon'[80])
  
except IndexError as error:
  print(error.__class__.__name__)
  
else: 
  print('Nothing wrong')
  
finally:
  print('Bylkers\n')

# 'else' will be executed when 'try' got no error
try:
  print('OOrreeggoonn'[0:12:2])
  
except IndexError as error:
  print(error.__class__.__name__)
  
else: 
  print('Nothing wrong')
  
finally:
  print('Bylkers')