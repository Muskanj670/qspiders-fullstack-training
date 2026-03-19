n = int(input("Enter a no: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="\t")
    for j in range((i*2)-1,0,-1):
        print(j,end='\t')
    print()