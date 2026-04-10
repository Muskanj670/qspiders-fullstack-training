def isKaprekar(n):
    sq = n**2
    l = len(str(sq))
    if l % 2 != 0:
        l += 1
    mid = l // 2

    if sq % (10**mid) + sq //(10**mid) == n:
        return True
    return False

n = int(input("Enter a number: "))
print(isKaprekar(n))