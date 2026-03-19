n = int(input("Enter a no: "))
pattenSize = 1
space = n//2
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(pattenSize):
        print("*",end=' ')
    if i < (n//2) :
        pattenSize += 1
        space -=1
    else: 
        pattenSize -= 1
        space += 1
    print()