num = int(input("Enter a number: "))
odd = ((num)*2) -1
for i in range(1, num+1):
    start = num - i + 1
    diff = (i-1)*2
    for j in range(1, i+1):
        print(start, end="\t")
        if j % 2 == 1:
            start += diff
            diff -= 4
        else:
            start += odd  
    odd -= 2
    print()

