n = int(input("Enter a num: "))
start = 1
even = 1
odd = 2
for i in range(1, n + 1):
    for j in range(1, i+1):
        print(start, end="\t")
        if i % 2 == 1:
            start += 1
        else:
            start -= 1
    print()
    if i % 2 == 1:
        start += (even*2) - 1
        even += 1
    else:
        start += odd*2 - 1
        odd += 1

    


