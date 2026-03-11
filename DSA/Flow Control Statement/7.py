year = int(input("Enter a year: "))
print(True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False )