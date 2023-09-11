questions = [
  {'Question': 'Which president of Brazil did not practice corruption?',
   'Options': ['Bandido, Bêbado, Condenado em três instâncias', 'Dilma Rousseff', 'Fernando Collor de Melo', 'Jair Messias Bolsonaro'],
   'Answer': 'Jair Messias Bolsonaro'
  },
  {
    'Question': 'Which is the latim name of car?',
    'Options': ['Catus felinus', 'Felis silvestris catus', 'Felinus catus', 'Felis catus silvestris'],
    'Answer': 'Felis silvestris catus'
  },
  {
    'Question': 'Which singer is known for making songs for intimate moments?',
    'Options': ['Olivia Rodrigo', 'Patati and Patata', 'The Weeknd', 'Al Bowlly'],
    'Answer': 'The Weeknd'
  }
]

'''The function 'valid_char_test' has a loop that ends when the letter corresponds
to an index, making 'index.get(answer, False)' becomes 'True' if the method 'get' can
find an  existing value. But, if its value is zero, is gets False. That's why the loop
has the 'and' logical operator, considering 'index.get(answer) == 0' too.'''
def valid_char_test(answer):
  while not index.get(answer, False) and index.get(answer) != 0:
    answer = input('Invalid. Try again: ')

index         = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
count_correct = 0
count_total   = 0

for question in questions:
  count_total  += 1
  correct_index = None
  for i, option in enumerate(question['Options']):
    if option == question['Answer']:
      correct_index = i
      break

  print(question['Question'])
  print(f'A) {question["Options"][0]}',
        f'B) {question["Options"][1]}',
        f'C) {question["Options"][2]}',
        f'D) {question["Options"][3]}',
        sep='\n', end='\n\n')

  answer = input('Choose an alternative: ')
  valid_char_test(answer)

  if index[answer] == correct_index:
    print('Correct answer, congratulations!', end='\n\n')
    count_correct += 1
  else:
    print('Wrong answer.', end='\n\n')
    
print(f'You made {count_correct} out of {count_total} questions.')
