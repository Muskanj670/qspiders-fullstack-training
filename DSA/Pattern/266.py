n = int(input("Enter a number: "))
mid = n//2 + 1
space = mid - 1
patternSize = 1
for i in range(1, n+1):
    if i <= mid:
        for j in range(1, space+1):
            print(end="  ")
        for j in range(1, patternSize+1):
            print("*",end=" ")
    else:
        print("  "*(mid-1) + "*")
    print()
    patternSize += 2
    space -= 1
        