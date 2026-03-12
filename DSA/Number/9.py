start = int(input("Enter a starting number: "))
stop = int(input("Enter an ending number "))

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True if n == i else False

def digitSum(n):
    sum = 0
    while n > 0:
        sum +=n % 10
        n //= 10
    return sum

def finalList(start,stop):
    c = 0
    l = []
    while start < stop:
        isPrime_ = isPrime(start)
        if isPrime_:
            isDigitPrime = isPrime(digitSum(start))
            if isDigitPrime:
                c += 1
                l.append(start)
        start += 1

    return c,l

print(finalList(start,stop))
    
