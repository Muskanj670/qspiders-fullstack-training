n = int(input("Enter a num: "))
patternSize = n//2 + 1
space = -1
for i in range(1, n + 1):
    for j in range(1,patternSize + 1):
        print("*", end=" ")
    for j in range(1, space + 1):
        if i == 1:
            continue
        print(" ", end=" ")
    for j in range(1, patternSize + 1):
        if (i == 1 or i == n) and j == patternSize:
            continue
        print("*", end=" ")
    print()
    if i <= n // 2:
        patternSize -= 1
        space += 2
    else:
        patternSize += 1
        space -= 2

    
    