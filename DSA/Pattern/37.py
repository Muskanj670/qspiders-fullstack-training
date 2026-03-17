n = int(input("Enter a num: "))
start = (n*(n+1))//2
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    for j in range(1,i+1):
        print(start , end= "\t")
        start -= 1
    print()