n = int(input("Enter a num: "))
start = 1
for i in range(1,n+1):
    print(start, end=", ")
    start = (start ** 2)  + 1
print("...")
