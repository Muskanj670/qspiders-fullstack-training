n = int(input("Enter a num: "))
for i in range(1, n + 1):
    start = n*n -i + 1
    for j in range(1, n + 1):
        print(start, end="\t")
        if j % 2 == 1:
            start -= 2*(n-i+1) - 1
        else:
            start -= 2*(i) -1
    print()