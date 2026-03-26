n = int(input("Enter a number: "))
start = n//2 +1
for i in range(n):
    num = start
    for j in range(n):
        print(num,end=" ")
