total_price = float(input("Enter a num: "))
if total_price >= 100000:
    print(total_price - ((40 * total_price)/100))
elif total_price >= 6000:
    print(total_price - ((30 * total_price)/100))
elif total_price >= 3000:
    print(total_price - ((20 * total_price)/100))
elif total_price >= 1:
    print(total_price - ((8 * total_price)/100))