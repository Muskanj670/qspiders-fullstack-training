a = int(input("Enter a num: "))
b = int(input("Enter a num: "))
c = int(input("Enter a num: "))
d = int(input("Enter a num: "))

largest = a if a > b and a > c and a > d else b if b > c and b > d else c if c > d else d

print(largest)