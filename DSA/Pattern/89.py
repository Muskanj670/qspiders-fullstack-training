n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    for j in range((i*2)-1):
        print(chr(ord('A')+((i*2)-1)-j-1),end="\t")

    print()