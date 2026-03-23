num = int(input("Enter a number: "))
start = num*(num + 1) // 2
odd = num*2 - 1
for i in range(1, num+1):
    val = start
    even = (i - 2)*2
    for j in range(1 , i+1):
        print(val, end="\t")
        if j % 2 == 1:
            val -= odd
        else:
            val -= even
            even -= 4
    print()
    odd -= 2 
    start -= 1

