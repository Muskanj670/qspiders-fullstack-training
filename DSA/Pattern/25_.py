n = int(input("Enter a num: "))
start = (n*(n+1))//2
for i in range(1,n+1):
    out = ''
    for j in range(i):
        out = str(start) +'\t' + out 
        start -= 1
    print(out)