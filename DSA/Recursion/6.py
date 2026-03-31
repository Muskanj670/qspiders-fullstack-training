def getCubeSum(n):
    if n == 1:
        return 1
    return n**3 + getCubeSum(n-1)

print(getCubeSum(100))