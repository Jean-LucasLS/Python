s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(f'union                  -> {s3}')

s4 = s1 & s2
print(f'intersection           -> {s4}')

s5 = s1 - s2 # Present values only in the left set
print(f'diference              -> {s5}')

s6 = s1 ^ s2 # Values that are not present in both
print(f'symmetric diference    -> {s6}')