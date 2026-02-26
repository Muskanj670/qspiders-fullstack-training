a = input("Enter a str: ")
a = a.split()
out = {}
i = 0
while(i < len(a)):
    out[a[i]] = a[i][::-1]
    i+= 1

print(out)