n = int(input("Enter the value of n:"))
r = int(input("Enter the value of c:"))

def getCombination(n,r):
    if r > n:
        return 0
    combination = 1
    for i in range(r):
        combination = combination * (n-i)//(i+1)
    
    return combination

print(getCombination(n,r))