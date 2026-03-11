x = int(input("Enter a side of a triangle: "))
y = int(input("Enter a side of a triangle: "))
z = int(input("Enter a side of a triangle: "))

print("Valid" if x+y > z and y+z > x and z + x > y else "Invalid")