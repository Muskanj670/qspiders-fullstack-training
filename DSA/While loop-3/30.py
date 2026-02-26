n = int(input("Enter a number: "))
b = bin(n)
print(f"No of 1s in binary of {n} is: {b.count('1')}")
print(f"No of 0s in binary of {n} is: {b.count('0')-1}")