n = int(input("Enter a no: "))
start = 64 + (n**2)
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="\t")
    for j in range((i*2)-1):
        print(chr(start),end='\t')
        start -= 1
    print()