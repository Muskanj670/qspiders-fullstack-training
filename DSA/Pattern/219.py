n = int(input("Enter a num: "))
start = 2
inc = 3
for i in range(1,n+1):
    print(start, end=", ")
    start += inc
    inc = inc * 2
print("...")