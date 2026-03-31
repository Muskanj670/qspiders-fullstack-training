def getDigit_R_to_L(n):
    if n == 0:
        return
    print(n%10)
    getDigit_R_to_L(n//10)

getDigit_R_to_L(3470)