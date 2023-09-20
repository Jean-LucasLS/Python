FILE_PATH = 'file/file_a.txt'

# file = open(FILE_PATH, 'w')
# file.close()

with open(FILE_PATH, 'a+', encoding='utf8') as file: # 'a+' do not erase the file content
  file.write('New line\n')