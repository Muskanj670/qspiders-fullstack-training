n = int(input("Enter a number: "))
start = n*(n+1)//2 - n+1
space = n-1
odd = 2*n - 1
sub_odd = n*2
sub_even = (n+1)*2

for i in range(1, n+1):
    for j in range(space):
        print(f'{' ':4}',end='')
    for j in range(1, i+1):
        print(f'{start:4d}', end='')
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            start += j*2
        else:
            start += odd

    print()
    space -= 1
    odd -= 2

  
