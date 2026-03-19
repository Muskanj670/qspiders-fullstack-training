n = int(input("Enter a no: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="\t")
    start = i-1
    for j in range((i*2)-1):
        print(start,end='\t')
        if j < i-1:
            start -= 1
        else:
            start += 1
    print()