a = int(input("Enter a num: "))
sum = 0
i = 1
while i < a :
    if a % i == 0:
        sum += i

    i += 1

if sum == a:
    print("Perfect number ")
else:
    print("Not a perfect Number")