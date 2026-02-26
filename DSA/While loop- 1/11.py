i = 1
c = 0 
while True:
    if i * i > 100:
        break
    print(i**2, end=" ")
    c+= 1
    i += 1
print("\nCount = ",c)