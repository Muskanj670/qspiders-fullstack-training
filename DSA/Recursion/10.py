def getDigit_L_to_R(n):
    if n == 0:
        return
    getDigit_L_to_R(n//10)
    print(n%10)

getDigit_L_to_R(3470)