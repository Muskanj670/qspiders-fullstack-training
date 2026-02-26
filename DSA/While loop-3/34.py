n = int(input("Enter a number: "))
while n > 0:
    rem= n % 10
    n//= 10
    rem2 = n % 10
    if rem == rem2:
        print("False")
        break
else:
    print("True")