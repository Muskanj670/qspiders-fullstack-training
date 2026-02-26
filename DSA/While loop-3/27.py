data = input("Enter a string: ")
i = 0
j = -1
while i < len(data)/2:
    if data[i] != data[j]:
        print("Not a palindrome")
        break
    i+= 1
    j += -1
else:
    print("Palindrome")