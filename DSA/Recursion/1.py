def ascending(n):
    if n == 0:
        return
    ascending(n-1)
    print(n)

ascending(10)