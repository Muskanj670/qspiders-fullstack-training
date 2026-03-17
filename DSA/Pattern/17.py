n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(i):
        print(i%2,end=" ")
    print()