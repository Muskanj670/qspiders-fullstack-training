a = int(input("Enter a number: "))
def prime_factors_Sum(n):
    factors = []
    for i in range(2, n+1):
        while n % i == 0:
            factors.append(i)
            n = n//i
    print(sum(factors))
prime_factors_Sum(a)