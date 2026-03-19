num = int(input("Enter a number: "))
patternSize = num
space = 0
for i in range(1,num+1):
    for j in range(space):
        print(" ",end="\t")
    for j in range(1,patternSize+1):
        print(chr(64 + j),end="\t")
    if i <= num//2:
        patternSize -= 2
        space += 1
    else:
        patternSize += 2
        space -= 1
    print()