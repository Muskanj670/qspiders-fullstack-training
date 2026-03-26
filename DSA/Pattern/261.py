n = int(input("Enter a number: "))
ans = []

for i in range(n+1):
    for j in range(n-i):
        print(f"{" ":2}",end="")
    level = [1] * (i + 1)
    for j in range(1, i):
        level[j] = ans[i-1][j-1] + ans[i-1][j]

    ans.append(level)
    for num in level:
        print(f"{num:<4}", end="")
    print()