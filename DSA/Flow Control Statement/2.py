a = int(input("Enter a num: "))
b = int(input("Enter a num: "))
c = int(input("Enter a num: "))

if a == b == c:
    print("All are equal")
else:
    print(a if a > b and a > c else b if b > c else c)
