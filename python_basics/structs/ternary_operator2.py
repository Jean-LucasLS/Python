digit = 9
cond1 = digit if digit <= 9 else 0
cond2 = digit if digit > 10 else 2
cond3 = 'Rubellus' if digit == 9 else 'DIGNITAS'
cond4 = 'Rubellus' if digit == 8 else 'DIGNITAS' if digit == 9 else 'Bylkers'
cond5 = 'Rubellus' if digit == 8 else 'DIGNITAS' if digit == 7 else 'Bylkers'

print(cond1, cond2, cond3, cond4, cond5, sep=' - ', end='')
print(' -', 'Digit is 8.' if digit == 8 else 'Digit is 9.' if digit == 9 else 'Digit is not 8 or 9.')