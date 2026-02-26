n = input("Enter a number: ")
largest = 9
i = 0
while i < len(n):
    if largest < int(n[i]):
        print("False")
        break
    largest = int(n[i])
    i+= 1
else:
    print("True")

