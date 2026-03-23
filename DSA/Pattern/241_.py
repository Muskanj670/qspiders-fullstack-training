num = int(input("Enter a num: "))
odd = (num*2) - 1
start = 1
for i in range(1,num+1):
    n = start
    diff = (i-2)*2
    for j in range(1,i+1):
        print(n,end="\t")
        if j % 2 == 1:
            n += odd
        elif j % 2 == 0:
            n += diff
            diff -= 4
    print()
    odd -= 2
    start += 1
    


    