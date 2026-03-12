def ifEven(a,i=0,out=[]):
    if i >= len(a):
        return out
    if type(a[i]) == int and a[i] % 2 == 0:
        out.append(a[i]**2)
    else:
        out.append(a[i])

    return ifEven(a,i+1,out)
print(ifEven([2,'hello',7,8,3+5j]))