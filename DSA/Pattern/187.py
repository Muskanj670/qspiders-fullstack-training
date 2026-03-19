num = int(input("Enter a number: "))
patternSize = num
space = 0
for i in range(1,num+1):
    for j in range(space):
        print(" ",end="\t")
    start = 1
    for j in range(1,patternSize+1):
        print(start,end="\t")
        if j <= patternSize//2:
            start +=1
        else:
            start -=1
    if i <= num//2:
        patternSize -= 2
        space += 1
    else:
        patternSize += 2
        space -= 1
    print()