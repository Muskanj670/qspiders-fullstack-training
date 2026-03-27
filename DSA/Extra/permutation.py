n = int(input("Enter the value of n:"))
r = int(input("Enter the value of c:"))

def getPermutation(n,r):
    if r > n:
        return 0
    permutation = 1
    for i in range(r):
        permutation = permutation * (n-i)
    
    return permutation

print(getPermutation(n,r))