a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))

def getBiggest(a,b):
    return a if a > b else b

print(getBiggest(getBiggest(a,b) , getBiggest(c,d)))