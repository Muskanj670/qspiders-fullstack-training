i = 1
sum = 0
while i <= 101:
    if i % 2 != 0:
        sum += 1/i
    i += 1
print(sum)