num = int(input("Enter a num: "))
largest = 0
smallest = 9
while num > 0 :
    if num % 10 > largest:
        largest = num % 10
    if num % 10 < smallest:
        smallest = num % 10
    num //= 10
print(largest-smallest)