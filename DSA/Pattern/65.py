n = int(input("Enter a num: "))
start = chr(ord("A") + ((n*(n+1))//2) -1)
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(start,end=" ")
        start = chr(ord(start)-1)
    print()