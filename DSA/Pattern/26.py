n = int(input("Enter a num: "))
var = "A"
for i in range(1,n+1):
    out = ''
    for j in range(1,i+1):
        out += var +" "
        var = chr(ord(var)+1)
    print(out)