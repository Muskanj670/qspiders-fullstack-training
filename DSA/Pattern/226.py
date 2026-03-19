n = int(input("Enter a num: "))
start = 1
inc = 2
for i in range(1, n + 1):
    print(start, end=", ")
    start+= inc
    inc *= 2
print("...")