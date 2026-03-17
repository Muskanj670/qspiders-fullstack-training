n = int(input("Enter a num: "))
mid = n//2 + 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == mid or j == mid or i == 1 or j == 1 or i == n or j == n or i == j or i+j == n+1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()