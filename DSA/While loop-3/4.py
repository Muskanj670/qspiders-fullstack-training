num = int(input("Enter a num: "))
while num > 0 :
    if num % 10 >= 5:
        print(num % 10)
    num //= 10