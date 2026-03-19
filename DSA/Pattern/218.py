n = int(input("Enter a num: "))
start = 2
inc = 2
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="\t")
    for j in range(i):
        print(start, end="\t\t")
        start += (inc)*2
        inc +=1
    print()