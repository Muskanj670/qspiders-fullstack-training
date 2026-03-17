def first10Multiples(a):
    count = 0
    for i in range(1,a):
        if a % i == 0 and count < 10:
            yield i
            count += 1

print(list(first10Multiples(500000)))
