n = int(input("Enter a num: "))
patternSize = 1
space = n // 2 
for i in range(1, n + 1):
    for k in range(1, space + 1):
        print(" ", end=" ")
    for j in range(1, patternSize + 1):
        if j == 1 or j == patternSize:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    if i <= n // 2:
        patternSize += 2
        space -= 1
    else:
        patternSize -= 2
        space += 1