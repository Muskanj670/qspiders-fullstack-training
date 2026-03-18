n = int(input("Enter a num: "))
start = chr(ord('A') + (n*(n+1)//2)-1)
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(n-i+1):
        print(start,end=" ")
        start = chr(ord(start)-1)
    print()