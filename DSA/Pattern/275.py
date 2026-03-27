n = int(input("Enter a number: "))
mid = n//2
space = n//2 - 1
patternSize = n
for i in range(n):
    for j in range(space):
        print("  ",end="")
    for j in range(1,patternSize+1):
        print("* ",end="")
    print()

    if i < mid-1:
        patternSize += 2
        space -= 1
    elif i >= mid:
        patternSize -= 2
        space += 1