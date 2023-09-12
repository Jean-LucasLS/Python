FILE_PATH = 'file/file_with_open.txt'

# file = open(FILE_PATH, 'w')
# file.close()

with open(FILE_PATH, 'w+', encoding='utf8') as file: # 'w' erase all the currennt file content
  print(type(file))
  file.write('Doc\nJucaju')
  file.seek(0,0) # Moves the cursos to the (0, 0) point
  print(file.read())
  file.writelines(
  ('\nLine 1\nLine 2\n', 'Line 3\nLine 4')
  )
  file.seek(0,0)
  print(file.read())