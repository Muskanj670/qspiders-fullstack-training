def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def getReverse(n):
    rev = 0
    temp = n
    while temp > 0:
        rem = temp % 10
        rev = rev*10 + rem
        temp //= 10

    return rev

def isEmirp(n):
    if (n != getReverse(n)) and (isPrime(n) and isPrime(getReverse(n))):
        print(f'{n} is Emirp Number...')
    else:
        print("Not a Emirp Number")


a = int(input("Enter a number: "))
isEmirp(a)