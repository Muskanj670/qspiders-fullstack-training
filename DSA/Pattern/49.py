n = int(input("Enter a num: "))
start = chr(ord("A") + ((n*(n+1))//2) -1)
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    out = ''
    for j in range(i):
        out = start +"\t" +out
        start = chr(ord(start)-1)
    print(out)