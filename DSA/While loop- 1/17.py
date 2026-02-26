n = int(input("Enter a number: "))
i = 1
c = 0
while i<=n:
    if n % i == 0:
        print(i, end=" ")
        c += 1
    i += 1
print(f"\nCount : {c}")