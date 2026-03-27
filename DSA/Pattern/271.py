n = int(input("Enter a num: "))
space = n//2
patternSize = 1
mid = n//2 +1
for i in range(1, n+1):
    for j in range(space):
        print("  ",end="")
    for j in range(1,patternSize+1):
        print("* ",end="")
    if i == 1:
        print("@ "*(n-2),end="")
    else:
        print("  "*(n-2),end="")
    for j in range(1,patternSize+1):
        print("* ",end="")
    print()

    if i < mid:
        space -= 1
        patternSize += 1
    else:
        space+=1
        patternSize -= 1