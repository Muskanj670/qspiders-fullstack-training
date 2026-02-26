i = 1
c = 0
while i < 1001:
    if i % 7 == 0 and i % 10 == 7:
        c += 1
        print(i, end=" ")
    i += 1

print("\nCount = ", c)