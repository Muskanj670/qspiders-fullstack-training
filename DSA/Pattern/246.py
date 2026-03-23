n = int(input("Enter a number: "))
start = (n*(n+1)//2) + 64
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(start), end="\t")
        if i % 2 == 1:
            start -= 1
        else:
            start += 1
    print()
    if i % 2 == 1:
        start -= i
    else:
        start -= i+1 