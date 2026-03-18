n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    out = ''
    for j in range(i):
        print(chr(ord('A')+n-i),end="\t")
    print()