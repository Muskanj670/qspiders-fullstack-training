def table(n,num = 1):
    if num ==11:
        return
    print(f'{n} * {num} = {n*num}')
    table(n,num+1)

table(5)
