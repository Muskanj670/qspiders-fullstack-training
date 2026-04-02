a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))

def getBiggest(a,b):
    return a if a > b else b

def getSmallest(a,b):
    return a if a < b else b

biggest = getBiggest(getBiggest(a,b) , getBiggest(c,d))
smallest = getSmallest(getSmallest(a,b) , getSmallest(c,d))

print(biggest, smallest)

def HCF(a,b):
    return a if b == 0 else HCF(b , a % b)

print(HCF(biggest,smallest))

