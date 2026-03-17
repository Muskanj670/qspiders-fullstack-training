n = int(input("Enter a num: "))
count = 1
for i in range(1,n+1):
    out = ''
    for j in range(i):
        out = str(count) + " " + out
        count += 1
    print(out)