a = 10
b = 20
c = 30

print("Before swapping: ",a,b,c)

#  Using fourth variable
temp = a
a = b
b = c
c = temp

print(a,b,c)

# Without fourth variable

a,b,c = b,c,a
print(a,b,c)

