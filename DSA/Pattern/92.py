n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    start = chr(ord('A')+i-1)
    for j in range((i*2)-1):
        print(start,end="\t")
        if j <i-1:
            start = chr(ord(start)-1)
        else:
            start = chr(ord(start)+1)
    print()