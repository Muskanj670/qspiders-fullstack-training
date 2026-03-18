n = int(input("Enter a num: "))
start = ((n*(n+1))//2) + (((n-1)*(n))//2)
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    for j in range((i*2)-1):
        print(start,end="\t")
        start -=1
    print()