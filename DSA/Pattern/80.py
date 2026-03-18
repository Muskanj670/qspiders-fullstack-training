n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    start = i
    for j in range((i*2)-1):
        print(start,end="\t")
        if j < i-1:
            start +=1
        else:
            start -=1
    print()