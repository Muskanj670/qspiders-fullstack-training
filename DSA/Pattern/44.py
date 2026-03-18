n = int(input("Enter a num: "))
start = 'A'
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    out = ''
    for j in range(i):
        print(start,end="\t")
        start = chr(ord(start)+1)
    print()