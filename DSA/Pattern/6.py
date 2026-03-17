n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i < 3 or i > n-2  or j < 3 or j > n-2:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()