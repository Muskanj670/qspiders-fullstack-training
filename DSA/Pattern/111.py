n = int(input("Enter a no: "))
count = 1
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="\t")
    for j in range((i*2)-1):
        print(count,end='\t')
        count += 1
    print()