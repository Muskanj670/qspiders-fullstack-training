a = int(input("Enter a num: "))
b = int(input("Enter a num: "))
c = int(input("Enter a num: "))

largest = a if a > b and a > c else b if b > c else c
smallest = a if a < b and a < c else b if b < c else c 
print ((a+b+c) - largest - smallest)