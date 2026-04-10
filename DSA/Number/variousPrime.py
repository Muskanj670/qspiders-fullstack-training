def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def getDigitSum(num):
    Sum = 0
    while num > 0:
        rem = num % 10
        Sum += rem
        num = num // 10
    return Sum

def primeInRange(a,b):
    count = 0
    for i in range(a, b+1):
        if isPrime(i):
            count += 1
            yield i

    print(f'Count = {count}')

def alternatePrimeAtOdd(a,b):
    count = 0
    for i in range(a, b+1):
        if isPrime(i):
            count += 1
            if count % 2 == 0:
                yield i

def alternatePrimeAtEven(a,b):
    count = 0
    for i in range(a, b+1):
        if isPrime(i):
            count += 1
            if count % 2 != 0:
                yield i

def primeWithDigitSumPrime(a,b):
    for i in range(a, b+1):
        if isPrime(i) and isPrime(getDigitSum(i)):
            yield i

def K_PrimeNum(a,b):
    k = int(input("Enter the value of K: "))
    count = 0
    for i in range(a, b+1):
        if isPrime(i):
            count += 1
            if count == k:
                return i
    else:
        return f"Does not contain {k} prime number in range {a} to {b}."

def getRotation(num):
    rem = num % 10
    num = num // 10
    return int(str(rem) + str(num))

def circularPrime(n):
    if isPrime(n):
        l = len(str(n))
        for i in range(l-2):
            n = getRotation(n)
            if not isPrime(n):
                return False
        return True
    else:
        return False


a = int(input("Enter Starting Value: "))
b = int(input("Enter ending Value: "))

print(f"\nPrime Number in range {a} to {b} are : {list(primeInRange(a,b))}")    
print(f"\nAlternate Prime Number at Odd position in range {a} to {b} are : {list(alternatePrimeAtOdd(a,b))}") 
print(f"\nAlternate Prime Number at Even position in range {a} to {b} are : {list(alternatePrimeAtEven(a,b))}")    
print(f"\nPrime Number in range {a} to {b} whose digit sum is also prime are : {list(primeWithDigitSumPrime(a,b))}")
print(f"\nK Prime Number in range {a} to {b} is : {K_PrimeNum(a,b)}")
print(f"\nIs {a} a circular Prime Number? : {circularPrime(a)}")

