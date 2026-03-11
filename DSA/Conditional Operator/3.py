n = int(input("Enter a num: "))
if n % 5 == 0 and n % 3 == 0 :
    print("Both")
elif n % 5 == 0:
    print(5)
elif n % 3 == 0:
    print(3)
else:
    print("None")