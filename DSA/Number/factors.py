a = int(input("Enter a number: "))
def factors(n):
    s = []
    l = []
    for i in range(1, int(n**0.5 )+ 1):
        if n % i == 0:
            s.append(i)
            if i != n //i:
                l.insert(0,n//i)
    print(s+l)
    print("Total Factors = " ,len(s+l))
    print("Sum of factors = ", sum(s) + sum(l))
factors(abs(a))