def difOfOne(a,i= 0,c = 0):
    if i >= len(a):
        return c
    if a[i] == '1':
        c += 1
    return difOfOne(a,i+1,c)

print(difOfOne("110011100101") - difOfOne("001100011010"))