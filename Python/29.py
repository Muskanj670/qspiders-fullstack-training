data = input("Enter a str: ")
out = ''
i = len(data)-1
print(i)
while i >= 0:
    out += data[i]
    i -= 1
if data == out:
    print("Palindrome")
else:
    print("No")
