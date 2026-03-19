n = int(input("Enter a num: "))
start = 1
for i in range(1, n + 1):
    print(start, end=", ")
    if i % 2 == 1:  # odd positions: add 1
        start += 1
    else:  # even positions: multiply by 3
        start *= 3
print("...")