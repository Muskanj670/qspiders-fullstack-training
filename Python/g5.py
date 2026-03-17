a = int(input("Enter a number: "))
def getFactorialValues(a):
    def factorial(i):
        if i < 1:
            return 1
        return i * factorial(i-1)
    
    for i in range(1, a):
        if factorial(i) <= a:
            yield [i,factorial(i)]
        else:
            return
        
print(dict(getFactorialValues(a)))