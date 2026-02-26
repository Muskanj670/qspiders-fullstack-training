data = eval(input("Enter a list: "))
out = []
i = 0
while (i < len(data)):
    if type(data[i]) in [str,tuple,list,set,dict]:
        out.append(len(data[i]))
    else:
        out.append(1)
    i+= 1
    
print(out)