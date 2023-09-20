def message1(msg, name):
  def closured_msg1():
    return f'\'{msg}\', by: {name}'
  return closured_msg1

msg1 = message1('It\'s cold', 'Dodger')
msg2 = message1('It\'s hot' , 'Jucaju')

print(msg1  , msg2  , sep=' #### ') # Variables store "unresolved" functions
print(msg1(), msg2(), sep=' #### ') # Executing variables as function calls requires the resolution of the "stored" functions

#### Deferring the passing of the 'name' parameter ####

def message2(msg):
  def closured_msg2(name):
    return f'\'{msg}\', by: {name}'
  return closured_msg2

msg3 = message2('It\'s cold')
msg4 = message2('It\'s hot' )

print(msg3  , msg4  , sep=' #### ')
print(msg3('Dodger'), msg4('Jucaju'), sep=' #### ')