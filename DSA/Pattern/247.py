n = int(input("Enter a num: "))
start = 65
odd = n*2 -1
for i in range(1, n+1):
    val = start
    diff = (i - 2)* 2
    for j in range(1, i+1):
        print(chr(val), end = ' ')
        if j % 2 == 1:
            val += odd
        else:
            val += diff
            diff -= 4
    print()
    start += 1
    odd -= 2


# 1
# 2   9
# 3   8   10
# 4   7   11  14
# 5   6   12  13  15