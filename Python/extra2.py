pwd = input("Enter your password: ")
l = len(pwd)
i = 0
size, num, upper = False,False,False
if l >= 8:
    size = True
    while i < l:
        if '0' <= pwd[i] <= '9':
            num = True
        elif 'A'<= pwd[i] <='Z':
            upper = True
        i += 1
    
if size and num and upper:
    print("Strong Pwd")
else:
    print("Try something else..")
