import json
import os

BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
SAVE_DIR = os.path.join(BASE_DIR, 'json_py.json')

person = {
  'name': 'Jucaju',
  'lastname': 'Doc',
  'age': 27,
  'addresses': [{'street 1': 'Wall Street'}, {'street 2': 'Luba Street'}],
  'telephones': {
    'residencial': 'xx xxxx-xxxx',
    'cell': 'xx xxxxx-xxxx'
  },
  'blood_type': 'A+'
}

# json_text = json.dumps(person, indent=2)
# print(json_text)

with open(SAVE_DIR, 'w', encoding='utf8') as file:
  json.dump(person, file, ensure_ascii=False, indent=2) # Never put this python file name as 'json.py'

with open(SAVE_DIR, 'r', encoding='utf8') as file:
  person_json = json.load(file)
  print(person_json)

