num = int(input("Enter a num: "))
c = 0
while num > 0 :
    rem = num % 10
    if rem >= 5:
        c += 1
    num //= 10
print(c)