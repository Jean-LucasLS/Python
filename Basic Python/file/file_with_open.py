FILE_PATH = 'file/file_with_open.txt'

# file = open(FILE_PATH, 'w')
# file.close()

# 'w' erase all the currennt file content IF a command to write in the file is given
with open(FILE_PATH, 'r', encoding='utf8') as file:
  print(type(file))
  file.write('Doc\nJucaju')
  file.seek(0,0) # Moves the cursos to the (0, 0) point
  print(file.read())
  file.writelines(
  ('\nLine 1\nLine 2\n', 'Line 3\nLine 4')
  )
  file.seek(0,0)
  print(file.read())