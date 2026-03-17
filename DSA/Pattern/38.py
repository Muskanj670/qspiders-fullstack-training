n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    for j in range(1,i+1):
        print(n-i+1 , end= "\t")
    print()