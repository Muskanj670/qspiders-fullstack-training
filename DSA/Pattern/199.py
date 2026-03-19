num = int(input("Enter a num: "))
patternSize = 1
space = num - 2
for i in range(1, num+1):
    for j in range(patternSize):
        print("*", end="")
    for j in range(space):
        print(" ", end="")
    for j in range(patternSize):
        if patternSize > num //2 and j == num//2:
            continue
        print("*", end="")
    if i <= num//2:
        patternSize += 1
        space -= 2
    else:
        patternSize -= 1
        space += 2
    print()