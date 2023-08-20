def message(msg, name): # A funçãp irá ler uma tupla, separando-a
  return f'{msg}, {name}!'

def execute(func, *args):
  print(f'args: {args} | type: {type(args)}')
  return func(*args)

print(execute(message, 'Hello', 'Jucaju'))