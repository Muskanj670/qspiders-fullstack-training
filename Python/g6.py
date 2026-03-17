a = int(input("Enter a number: "))  
def getPrimeInrange(a):
    def prime(i):
        if i == 1:
            return False
        for j in range(2,i):
            if i % j == 0:
                return False
        return True
        
    for i in range(1,a):
        if prime(i):
            yield i

print(list(getPrimeInrange(a)))