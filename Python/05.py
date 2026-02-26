a = eval(input("Enter a set: "))
print(a)

b = eval(input("Enter a value to be inserted: "))
a.add(b)
print(a)

c = eval(input("Enter a value to be deleted: "))
a.remove(c)
print(a)