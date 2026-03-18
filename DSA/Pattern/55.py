n = int(input("Enter a num: "))
start = 1
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    for j in range(1,i+1):
        print(start,end="\t\t")
        start += 1
    print()