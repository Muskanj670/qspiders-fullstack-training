n = int(input("Enter a number: "))
start = n*(n+1)//2
space = n - 1
odd = 2
even = 2
for i in range(1, n+1):
    for j in range(space):
        print(end="\t")
    for j in range(1, i+1):
        print(start, end="\t")
        if i % 2 == 1:
            start += 1
        else:
            start -= 1
    print()
    space -= 1
    if i % 2 == 1:
        start -= odd
        odd += 2
    else:
        start -= even
        even += 2 
