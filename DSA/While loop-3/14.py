n = input("Enter a number: ")
i = 0
n = int(n[::-1])
while n > 0:
    print(n%10)
    n //= 10
