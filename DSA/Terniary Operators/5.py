a = int(input("Enter a side of a triangle: "))
b = int(input("Enter a side of a triangle: "))
c = int(input("Enter a side of a triangle: "))

ans = True if a+b >c and b+c> a and a+c > b else False
print(ans)