l = eval(input("Enter a list: "))
for i in range(len(l)):
    if type(l[0]) != type(l[i]):
        print("Hetero")
        break
else:
    print("Homo")