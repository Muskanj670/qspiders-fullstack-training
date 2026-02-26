num = int(input("Enter a num: "))
while num > 0 :
    if num % 2 == 0 :
        print(num % 10)
    num //= 10
