a = eval(input("Enter the data: "))
if (a%5 == 0):
    if(a%2 == 0):
        print("True")
    else:
        print("Div by 5 but odd")
else:
    print("False")