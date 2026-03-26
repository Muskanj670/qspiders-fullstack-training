n = int(input("Enter a number: "))
mid = n//2 
space_1 = mid 
start = 1
for i in range(1, n+1):
    for j in range(space_1):
        print(end = "  ")
    for j in range(start):
        print("*",end = " ")
    if i == 1:
        print("@ "*mid , end="")
    else:
        print("  "*mid , end="")
    if i <= mid+1:
        print("@", end=" ")
    else:
        print(" " , end=" ")
    if i > mid+1:
        for j in range(mid+2):
            print("*", end=" ")
    else:
        for j in range(mid+2):
            print(" ", end=" ")
    if i <= mid+1:
        print("@", end=" ")
    else:
        print(" " , end=" ")
    if i == 1:
        print("@ "*mid , end="")
    else:
        print("  "*mid , end="")
    for j in range(start):
        print("*",end = " ")
    
    print()

    if i <= mid:
        space_1 -=1
        start += 1
    else:
        space_1 += 1
        start -= 1
    

