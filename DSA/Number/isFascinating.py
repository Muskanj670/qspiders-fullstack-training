def isFascinating(n):
    final = str(n) + str(n*2) + str(n*3)
    if len(final) == 9 and len(set(final)) == 9:
        for i in range(1,10):
            if str(i) not in final:
                return False
        return True
    return False

a = int(input("Enter a num: "))
print(isFascinating(a))
