def power(num,pow):
    if pow == 1:
        return num

    return num * power(num,pow-1)

print(power(8,3))