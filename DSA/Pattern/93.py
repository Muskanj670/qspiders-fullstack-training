n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(n-i+1):
        print("*",end=" ")
    print()