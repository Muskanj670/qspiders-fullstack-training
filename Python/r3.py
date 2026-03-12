def extractNum(a,i=0,out=[]):
    if i >= len(a):
        return out
    if type(a[i]) is int:
        out.append(a[i])
    return extractNum(a,i+1,out)

print(extractNum([1,2,3,'helo',3+5j,4]))