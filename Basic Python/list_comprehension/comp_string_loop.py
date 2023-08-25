main_string = 'Joseph Willford'
letter_step = 2
new_string  = '-'.join([
  main_string[index:index + letter_step]
  for index in range(0, len(main_string), letter_step)
])
print(new_string)

upper_list = ['JUCAJU', 'DIGNITAS', 'BORIS JOHNSON', 'DOMENICO']
lower_list = [
  name.title() for name in upper_list
]
print(lower_list)

last_upper = [
  name[:-1].lower() + name[-1].upper() for name in lower_list
  #f'{name[:-1].lower(){name[-1].upper()}}' for name in lower_list
]
print(last_upper)