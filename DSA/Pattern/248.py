n = int(input("Enter a number: "))
start = 64 + (n*(n+1)//2)
odd = 2*n - 1
for i in range(1, n+1):
    val = start
    diff = (i -2)*2
    for j in range(1, i+1):
        print(chr(val), end=" ")
        if j % 2 == 1:
            val -= odd
        else:
            val -= diff
            diff -= 4
    print()
    start -= 1
    odd -= 2


# 15
# 14  7
# 13  8  6
# 12  9  5  2
# 11  10  4  3   1