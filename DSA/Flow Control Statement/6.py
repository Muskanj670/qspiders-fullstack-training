x = int(input("Enter a side of a triangle: "))
y = int(input("Enter a side of a triangle: "))
z = int(input("Enter a side of a triangle: "))

isValid = True if x+y > z and y+z > x and z + x > y else False

if isValid: 
    if x == y == z:
        print("Equilateral")
    elif x == y or y == z or x == z:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid Triangle")