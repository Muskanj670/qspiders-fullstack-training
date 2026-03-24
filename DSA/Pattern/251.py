n = int(input("Enter a num: "))
space = n - 1
num = 1
odd = 2*n - 1
add_odd = n*2
add_even = (n+1)*2
for i in range(1, n+1):
    for j in range(space):
        print(end="\t")
    for j in range(1, i+1):
        print(num, end="\t")
        if (j % 2 == 0 and i % 2 == 1) or (j % 2 == 1 and i % 2 == 0):
            num -= odd
        else:
            num -= j*2
    print()
    space -= 1
    odd -= 2

    if i % 2  == 1:
        num += add_odd
        add_odd += odd
    else:
        num += add_even
        add_even += odd + 2
