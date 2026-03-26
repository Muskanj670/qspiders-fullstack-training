n = int(input("Enter a number: "))
space = n-1
start = 65

for i in range(1, n+1):
    for j in range(space):
        print(end='  ')
    for j in range(1, i+1):
        print(chr(start),end=" ")
        if i % 2 == 1:
            start -= 1
        else:
            start += 1

    print()
    if i % 2 == 1:
        start += i+1
    else:
        start += i 
    space -= 1