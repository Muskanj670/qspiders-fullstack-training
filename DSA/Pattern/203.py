num = int(input("Enter a num: "))
patternSize = 1
space = num - 2
for i in range(1, num+1):
    val = 1
    for j in range(patternSize):
        print(val % 2, end=" ")
        val += 1
    for j in range(space):
        print(" ", end=" ")
        val += 1
    for j in range(patternSize):
        if patternSize > num //2 and j == 0:
            continue
        print(val % 2, end=" ")
        val += 1
    if i <= num//2:
        patternSize += 1
        space -= 2
    else:
        patternSize -= 1
        space += 2
    print()