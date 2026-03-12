n = int(input("Enter a num: "))
sq = n ** 2
ln = len(str(n))
print(True if n == sq % (10**ln) else False)
