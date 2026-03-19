n = int(input("Enter a num: "))
start = 2
for i in range(n):
    print(start, end=", ")
    start += (i+2)*2
print("...")