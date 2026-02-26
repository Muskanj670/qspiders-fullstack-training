a = input("Enter a str: ")
i = 0
c = 0
while i < len(a):
    if a[i] == '(':
        c += 1
    elif a[i] == ')':
        c -= 1

    i += 1
print (abs(c))
