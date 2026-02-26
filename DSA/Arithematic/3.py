a = 5
b = 7

print("Before Swapping: ", a,b)
# With third variable
temp = a
a = b
b = temp

print(a,b)

# Without third variable

b, a = a,b
print(a,b)
