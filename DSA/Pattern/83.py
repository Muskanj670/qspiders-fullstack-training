n = int(input("Enter a num: "))
start = 1
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    for j in range((i*2)-1):
        if i == j+1:
            print(1,end="\t")
        else:
            print(start,end="\t")
            start += 1
    print()