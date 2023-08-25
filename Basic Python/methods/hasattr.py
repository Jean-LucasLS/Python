# hasattr() tests if a method can be applyed to a given variable
string  = 'Jucaju'
integer = 12

if hasattr(string, 'upper'):
  print(string.upper())
  
if hasattr(integer, 'upper'):
  print(integer.upper())