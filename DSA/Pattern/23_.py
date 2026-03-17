n = int(input("Enter a num: "))
start = (n*(n+1))//2
for i in range(1,n+1):
    for j in range(i):
        print(start,end="\t")
        start -= 1
    print()