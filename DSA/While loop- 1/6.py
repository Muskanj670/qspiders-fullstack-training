i = 1
c = 0
while i < 101:
    if i % 7 == 0:
        c += 1
        print(i, end=" ")
    i += 1

print("\nCount = ", c)