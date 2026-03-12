# WAP to extract all the upper case from a string

def up(a,i = 0, out = ''):
    if i >= len(a):
        return out
    if 'A' <= a[i] <= 'Z':
        out += a[i]
    return up(a,i+1,out)

print(up("Hello World"))