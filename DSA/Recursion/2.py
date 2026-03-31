def descending(n):
    if n == 0:
        return
    print(n)
    descending(n-1)

descending(10)