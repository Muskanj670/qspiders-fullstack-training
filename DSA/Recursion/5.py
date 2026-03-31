def getSquareSum(n):
    if n == 1:
        return 1
    return n**2 + getSquareSum(n-1)

print(getSquareSum(100))