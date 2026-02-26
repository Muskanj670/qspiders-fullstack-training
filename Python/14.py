c = input("Enter char: ")
if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
    if c in 'aeiouAEIOU':
        print("Vowel")
    else:
        print('Consonant')
else:
    print("Not an alphabet")