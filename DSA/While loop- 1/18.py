num = int(input("Enter a num: "))
i = 2
if num == 1:
    print("Not prime")
elif num in [2,3]:
    print("Prime")
else:
    while i < num:
        if num % i == 0:
            print("Not Prime")
            break
        i += 1
    if i == num:
        print("Prime")