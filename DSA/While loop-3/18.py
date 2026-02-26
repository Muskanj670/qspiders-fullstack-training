n = int(input("Enter a number: "))
c = 0
while n > 0:
    rem = n % 10
    if rem % 2 != 0:
        c += rem
    n //= 10
print(c)