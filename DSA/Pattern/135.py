n = int(input("Enter a no: "))
pattenSize = 1
space = n//2
start = (((space+1)*(space+2))//2) + ((space*(space+1))//2)
for i in range(1,n+1):
    for j in range(space):
        print(" ",end="\t")
    for j in range(1,pattenSize+1):
        print(start,end='\t\t')
        start -= 1
    if i-1 < (n//2) :
        pattenSize += 1
        space -=1
    else: 
        pattenSize -= 1
        space += 1
    print()