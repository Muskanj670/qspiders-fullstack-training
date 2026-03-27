n = int(input("Enter a num: "))
mid = n//2
mid2 = n - (mid+1)//2
space1 = mid - 2
patterSize1 = 1
space2 = (mid+1)//2
patterSize2 = 1

for i in range(1, n+1):
    if i >= mid - 1:
        for j in range(space1):
            print("  ",end="")
        for j in range(patterSize1):
            print("* ",end="")
    else:
        for j in range(mid-1):
            print("  ",end="")
    
    if i == mid - 1:
        print("@ "*mid,end="")
    else:
        print("  "*mid,end="")

    if i < mid:
        for j in range(space2):
            print("  ",end="")
        for j in range(patterSize2):
            print("* ",end="")

    print()
    if i >= mid - 1:
        if i <mid2:
            space1 -= 1
            patterSize1 += 1
        else:
            space1 +=1
            patterSize1 -= 1

    if i < mid:
        space2 -= 1
        patterSize2 += 2