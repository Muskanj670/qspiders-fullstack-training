n = int(input("Enter a no: "))
pattenSize = 1
for i in range(n):
    for j in range(pattenSize):
        print("*",end=' ')
    if i < (n//2) :
        pattenSize += 1
    else: 
        pattenSize -= 1
    print()