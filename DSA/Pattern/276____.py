n = int(input("Enter a num:"))
mid = n//2 +1
mid2 = mid//2
patternSize = 2
space = mid2 // 2
space2 = 0

for i in range(1,n+1):
    if i <= mid2:
        for j in range(space):
            print(" ",end="")
        for j in range(patternSize):
            print("*",end="")
        for j in range(2*space +1):
            print(" ",end="")
        for j in range(patternSize):
            print("*",end="")

    else:
        for j in range(space2):
            print(" ",end="")
        for j in range((n-i)*2 +1):
            print("*",end="")


    print()
    if i <= mid2:
        patternSize += 2
        space -=1
    else:
        space2 += 1