a = eval(input("Enter a dic: "))
print(a)

b = eval(input("Enter key: "))
c = eval(input("Enter new value: "))
a[b] = c
print(a)

b = eval(input("Enter new key: "))
c = eval(input("Enter value: "))
a[b] = c
print(a)

b = eval(input("Enter a key to be deleted: "))
del a[b]
print(a)

b = eval(input("Enter a dic: "))
a.update(b)
print(a)

print(a.values())
print(a.keys())
print(a.items())