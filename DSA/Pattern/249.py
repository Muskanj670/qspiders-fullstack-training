n = int(input("Enter a number: "))
space = n - 1
num = 1
odd,even = 2, 2
for i in range(1, n + 1):
    for j in range(1, space + 1):
        print(end="\t")
    for k in range(1, i+1):
        print(num, end="\t")
        if i % 2 == 1:
            num -= 1
        else:
            num += 1
    print()
    space -= 1
    if i % 2 == 0:
        num += odd
        odd += 2
    else:
        num += even
        even += 2
    