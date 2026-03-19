n = int(input("Enter a num: "))
start_1 = 0
start_2 = 0
start_3 = 1
for i in range(1, n + 1):
    print(start_1, end=", ")
    start_1, start_2, start_3 = start_2, start_3, start_1 + start_2 + start_3
print("...")