n = int(input("Enter a no: "))
pattenSize = 1
space = n//2
start = 65
for i in range(1,n+1):
    for j in range(space):
        print(" ",end="\t")
    val = start
    for j in range(1,pattenSize+1):
        print(chr(val),end="\t")
        if j <= pattenSize//2:
            val -= 1
        else:
            val +=1
    if i-1 < (n//2) :
        pattenSize += 2
        space -=1
        start += 1
    else: 
        pattenSize -= 2
        space += 1
        start -=1
    print()