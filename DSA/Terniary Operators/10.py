a = input("Enter a character: ")
ans = "Uppercase" if "A" <= a <= 'Z' else "Lowercase" if 'a' <= a<= 'z' else 'Digit' if '0' <= a <= '9' else 'Special Characer'
print(ans)