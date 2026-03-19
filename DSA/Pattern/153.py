n = int(input("Enter a no: "))
pattenSize = 1
space = n//2
for i in range(1,n+1):
    for j in range(space):
        print(" ",end="\t")
    for j in range(1,pattenSize+1):
        print(n-i+1,end='\t')
    if i-1 < (n//2) :
        pattenSize += 2
        space -=1
    else: 
        pattenSize -= 2
        space += 1
    print()