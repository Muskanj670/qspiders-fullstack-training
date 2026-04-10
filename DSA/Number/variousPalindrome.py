def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def isPalindrome(n):
    rev = 0
    temp = n
    while temp > 0:
        rem = temp % 10
        rev = rev*10 + rem
        temp //= 10

    return True if rev == n else False

def isPrimePalindromeInRange(a,b):
    for i in range(a, b+1):
        if isPrime(i) and isPalindrome(i):
            yield i

a = int(input("Enter staring num: "))
b = int(input("Enter ending num: "))

print(list(isPrimePalindromeInRange(a,b)))
