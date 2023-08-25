def generator1(n=0):
  yield 1 # Pause
  return 'it\'s end'

gen1 = generator1(n=0)
# print(gen1); print(gen1.__iter__()); print(next(gen1)); print(next(gen1))

#### Multiple yields ####

def generator2(n=0):
  yield 1 # Pause
  print('Continue...')
  yield 2 # Pause
  print('One more...')
  yield 3 # Pause
  print('Stop!')
  return 'Jucaju'

gen2 = generator2(n=0)
# print(next(gen2)); print(next(gen2)); print(next(gen2)); print(next(gen2))

for i in gen2:
  print(i)
  
def generator3(n=0, maximum=10):
  while True:
    yield n
    n += 1
    if n >= maximum:
      return

gen3 = generator3(n=8, maximum=15)
for i in gen3:
  print(i, end=' ')