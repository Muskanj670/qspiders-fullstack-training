a = input("Enter a str: ")
b = input("Enter a str: ")
i = 0
res = ''

while i < len(a) or i < len(b):
    if i < len(a):
        res += a[i]
    if i < len(b):
        res += b[i]
    i += 1

print(res)


