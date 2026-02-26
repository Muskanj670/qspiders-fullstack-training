a = input("Enter a str: ")
a = a.split()
out = {}
i = 0
while(i < len(a)):
    if i%2 == 0:
        out[a[i]] = a[i][::-1]
    else:
        out[a[i]] = len(a[i])*2
    i+= 1

print(out)