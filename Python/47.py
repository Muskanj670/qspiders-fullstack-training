a = eval(input("Enter a number list: "))
def fact(a):
    if a <= 1:
        return 1
    return  a * fact(a-1)

def getFact (a):
    out = []
    for i in a:
        out.append(fact(i))
    return out

print(getFact(a))

def newFact(a,out=[],i = 0):
    def fact(a):
        if a <= 1:
            return 1
        return  a * fact(a-1)
    if i >= len(a):
        return out
    out.append(fact(a[i]))
    return newFact(a,out,i+1)

print(newFact(a))
