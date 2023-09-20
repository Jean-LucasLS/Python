person = {
  'name': 'Jucaju',
  'lastname': 'DIGNITAS'
}

person_add = {
  'age': 27,
  'height': 1.8
}

person_info = {**person, **person_add, 'random_key': 4} # The double '**' unpacks dicts inside other dict declaration
print(person_info)