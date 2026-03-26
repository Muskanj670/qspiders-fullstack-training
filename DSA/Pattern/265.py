n = int(input("Enter a number: "))
mid = n//2 
space_1 = mid 
space_2 = -1
start = 1
start_2 = n 
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
        for j in range(space_2):
            print(end="  ")
        for j in range(start_2):
            print("*", end=" ")
        for j in range(space_2):
            print(end="  ")
    else:
        for j in range(n-2):
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
        start_2 -= 2
        space_2 += 1
    

