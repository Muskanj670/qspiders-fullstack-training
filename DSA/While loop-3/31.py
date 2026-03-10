n = int(input("Enter a number: "))
binary = ''
while n > 0 :
    bit = n % 2
    binary = str(bit) + binary
    n //= 2

print(binary)