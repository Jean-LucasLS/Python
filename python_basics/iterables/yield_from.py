def gen1():
  print('gen1 started!')
  yield 1
  yield 2
  yield 3
  print('gen1 ended...')
  
def gen2():
  yield from gen1()
  print('gen2 started!')
  yield 4
  yield 5
  yield 6
  print('gen2 ended...')
  
def gen3():
  yield from gen2()
  print('gen3 started!')
  yield 7
  yield 8
  yield 9
  print('gen3 ended.')

g = gen3()
for num in g:
  print(num)