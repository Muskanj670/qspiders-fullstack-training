n = int(input("Enter a number: "))
c = 0
temp = n
while n > 0:
    rem = n % 10
    c = c*10 + rem
    n //= 10

print(c== temp)