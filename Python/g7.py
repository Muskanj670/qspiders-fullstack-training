a = int(input("Enter a number: "))
def getPerfect(a):
    def isPerfect(i):
        sum = 0
        for j in range(1,i):
            if i % j == 0:
                sum += j
        return True if sum == i else False
    for i in range(1,a):
        if isPerfect(i):
            yield i

print(list(getPerfect(a)))