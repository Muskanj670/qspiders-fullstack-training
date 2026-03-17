n = int(input("Enter a num: "))
for i in range(1,n+1):
    out = ''
    for j in range(1,i+1):
        print(chr(ord("A")+i-j),end=" ")
    print()