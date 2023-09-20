from itertools import groupby

students = [
  {'name': 'Jucaju', 'grade': 'A'},
  {'name': 'Bylkers', 'grade': 'C'},
  {'name': 'Doc', 'grade': 'A'},
  {'name': 'Willford', 'grade': 'B'},
  {'name': 'Dodger', 'grade': 'E'},
  {'name': 'Domenico', 'grade': 'C'},
  {'name': 'Lockwood', 'grade': 'E'},
  {'name': 'Malke', 'grade': 'C'}
]

def ordering_by_grade(student):
  return student['grade']

sorted_students = sorted(students, key=ordering_by_grade)
print(sorted_students)

groups = groupby(sorted_students, key=ordering_by_grade)

for key, group in groups:
  print(key)
  for student in group:
    print(student)