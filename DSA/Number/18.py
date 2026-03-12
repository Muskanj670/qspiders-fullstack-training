n = input("Enter a number: ")
sum = 0
for i in range(len(n)):
    sum += int(n[i])**(i+1)

print("Disarium" if n == str(sum) else "Not")