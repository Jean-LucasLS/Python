def add_clients(name, list=[]): # Should not use mutable parameters on function default parameters ('list=[]')
  list.append(name)
  return list

client1 = add_clients('Jucaju')
add_clients('Doc', client1)
add_clients('Bylkers')
print(client1)

client2 = add_clients('Johnny')
add_clients('Markon', client2)
print(client2)

print('#' * 80)

def add_clients2(name, list=None): # Should not use mutable parameters on function default parameters ('list=[]')
  list.append(name)
  return list

list3 = []
client3 = add_clients('Jucaju', list3)
add_clients('Doc', client3)
add_clients('Bylkers')
print(client3)

list4 = []
client4 = add_clients('Johnny', list4)
add_clients('Markon', client4)
print(client4)