n = int(input("Enter a num: "))
start_1 = 0
start_2 = 1
for i in range(1, n + 1):
    print(start_1, end=", ")
    start_1, start_2 = start_2, start_1 + start_2
print("...")