n = int(input("Enter a no: "))
pattenSize = 1
space = n//2
start = 1
for i in range(1,n):
    for j in range(space):
        print(" ",end="\t")
    for j in range(1,pattenSize+1):
        if j == pattenSize//2 +1 or i == n//2 +1:
            print("*",end="\t")
        else:
            print(start,end="\t")
            start += 1
    if i-1 < (n//2) :
        pattenSize += 2
        space -=1
    else: 
        pattenSize -= 2
        space += 1
    print()