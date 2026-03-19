num = int(input("Enter a number: "))
patternSize = num
space = 0
start = num//2 +1
for i in range(1,num+1):
    for j in range(space):
        print(" ",end="\t")
    for j in range(1,patternSize+1):
        print(start,end="\t")
    if i <= num//2:
        patternSize -= 2
        space += 1
        start -= 1
    else:
        patternSize += 2
        space -= 1
        start +=1
    print()