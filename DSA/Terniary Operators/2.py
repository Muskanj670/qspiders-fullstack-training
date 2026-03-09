a = int(input("Enter a num: "))
b = int(input("Enter a num: "))
c = int(input("Enter a num: "))

#  Detail Description
if a >b and a >c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

# OR
x = a if a>b and a>c else (b if b > c else c)
print(x)

# OR
x = a if a>c else c if a>b else b if b>c else c
print(x)

# OR
x = a if a > b else b
print(x if x > c else c)