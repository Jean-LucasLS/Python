def message(msg, name): # The function will read a tuple, separating it
  return f'{msg}, {name}!'

def execute(func, *args):
  print(f'args: {args} | type: {type(args)}')
  return func(*args)

print(execute(message, 'Hello', 'Jucaju'))