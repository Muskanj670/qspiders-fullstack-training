a = eval(input("Enter a list: "))
b = []
c = []
i = 0
while i < len(a):
    if a[i] not in b:
        b.append(a[i])
    if a[i] not in c and a.count(a[i]) > 1:
        c.append(a[i]) 

    i += 1

print(b)
print(c)