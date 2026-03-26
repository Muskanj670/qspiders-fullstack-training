n = int(input("Enter a number: "))
space = n-1
start = 65
odd = 2*n - 1
add_odd = n*2
add_even = (n+1)*2
for i in range(1, n+1):
    for j in range(space):
        print(end="  ")
    for j in range(1, i+1):
        print(chr(start),end=" ")
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            start -= odd
        else:
            start -= j*2

    print()
    space -= 1
    if i%2 == 1:
        start += add_odd
        add_odd += odd - 2
    else:
        start += add_even
        add_even += odd
    odd -= 2
