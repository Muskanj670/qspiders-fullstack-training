n = input("Enter a number: ")
lowest = 0
i = 0
while i < len(n):
    if lowest > int(n[i]):
        print("False")
        break
    lowest = int(n[i])
    i+= 1
else:
    print("True")

