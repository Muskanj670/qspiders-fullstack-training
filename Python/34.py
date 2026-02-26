a = eval(input("Enter a list : "))
op = {}
i = 0
while i < len(a):
    if type(a[i]) is str:
        if i % 2 == 0 :
            op[a[i]] = len(a[i])
        else:
            op[a[i]] = a[i][::-1] + str(len(a[i])*2)
    i += 1

print(op)
