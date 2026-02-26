#WAP TO CHECK SPECIAL CHARACTER
b = [int, float,complex,bool]
a = eval(input("Enter a number: "))  
if (type(a) not in b):
    print("Multivalue...")
else:
    print("Single")