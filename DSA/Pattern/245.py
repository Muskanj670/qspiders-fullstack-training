n = int(input("Enter a number: "))
start = 65
patternSize = 1
for i in range(1, n+1):
    for j in range(patternSize):
        print(chr(start), end=" ")
        if patternSize % 2 == 1:
            start += 1
        else:
            start -= 1
    print()
    if patternSize % 2 == 1:
        start += patternSize 
    else:
        start += patternSize + 1
    patternSize += 1
