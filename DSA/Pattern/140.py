n = int(input("Enter a no: "))
pattenSize = 1
space = n//2
for i in range(1,n+1):
    for j in range(space):
        print(" ",end="\t")
    for j in range(1,pattenSize+1):
        print(chr(64+i),end='\t\t')
    if i-1 < (n//2) :
        pattenSize += 1
        space -=1
    else: 
        pattenSize -= 1
        space += 1
    print()