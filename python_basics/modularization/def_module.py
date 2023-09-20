def test_main():
  if __name__ != '__main__':
    print(f'This module\'s name is {__name__}')
  else:
    print('This is NOT main!')