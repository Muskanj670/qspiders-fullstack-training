def isPronic(n):
    i = 1
    while (i * (i+1) <= n):
        if i *(i+1) == n:
            return True

        i += 1
    return False

a = int(input("Enter a number: "))
print(isPronic(a))