num = 50
while True:
    n = int(input("Enter a num: "))
    if n < num:
        print("Think bigger....")
    elif n > num:
        print("You expercted a lot....")
    else:
        print("Yureka!, You won")
        break