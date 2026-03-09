n = int(input("Enter a number: "))
ans = "Divisible by both" if n % 5 == 0 and n % 3 == 0 else \
"Divisible by 5" if n % 5 == 0 else \
"Divisible by 3" if n % 3 == 0 else \
"Divisible by None"
print(ans)