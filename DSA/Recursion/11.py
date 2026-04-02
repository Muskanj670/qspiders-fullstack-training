def getDigitCount(n):
    return 1 if n < 10 else 1+ getDigitCount(n//10)
print(getDigitCount(345270))