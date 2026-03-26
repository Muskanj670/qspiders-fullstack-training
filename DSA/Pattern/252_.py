n = int(input("Enter a number: "))
space = n-1
ps = 1

def get_num(n,i,j):
    num = 0
    for k in range(1, n-j+1):
        num = num + n - k + 1
    
    if j % 2 == 1:
        num = num + n - i + 1- j- 1
    else:
        num = num + n + i + 1
    return num

for i in range(1, n+1):
    for j in range(space):
        print(f'{" ":4}',end="")
    for j in range(1, ps+1):
        print(f'{get_num(n,i,j):4d}',end="")
    print()
    space -= 1
    ps += 1



