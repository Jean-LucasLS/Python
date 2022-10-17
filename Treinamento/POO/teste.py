from personclass import Person
p1 = Person('Jonas', 8)
p2 = Person('James', 1)
p1.name = 'Jean'
p2.name = 'Joe'
p1.age = 26
p2.age = p1.age
p1.Printer()
p2.Printer()