import os

FILE_PATH1 = 'file/file_with_open.txt'
FILE_PATH2 = 'file/file_a.txt'

os.unlink(FILE_PATH1) # or 'os.remove(FILE_PATH)'
os.rename(FILE_PATH2, 'file/file_a_renamed.txt') # It can move the file to a new path too