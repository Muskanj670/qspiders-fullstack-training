def getDigitSum(n):
    if n < 10:
        return n

    return n%10 + getDigitSum(n//10)

print(getDigitSum(3470))