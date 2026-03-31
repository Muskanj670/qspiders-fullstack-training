def getDigitCount(n, count = 0):
    if n < 10:
        return count+1
    return getDigitCount(n//10, count+1)
print(getDigitCount(345270))