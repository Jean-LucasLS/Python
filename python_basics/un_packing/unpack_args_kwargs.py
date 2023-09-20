# kwargs -> keyword arguments
def show_key_arguments(*args, **kwargs):
  print(f'*args    -> {args}\n**kwargs -> {kwargs}\n')
  
show_key_arguments('Wilford', 'Hominem', name='Jucaju', lastname='DIGNITAS')

person = {
  'name': 'Bylkers',
  'lastname': 'Domenico'
}

show_key_arguments(*person, **person)
show_key_arguments(*person.items(), **person)