n = int(input("Enter a num: "))
start = 3
inc = 2
for i in range(1,n+1):
    print(start, end=", ")
    start += inc
    inc = inc * 2
print("...")