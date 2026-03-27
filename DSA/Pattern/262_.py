n = int(input("Enter a number: "))
mid = n//2 + 1
start = 1
end = n
for i in range(1,n+1):
    num = mid
    for j in range(1,n+1):
        if j < start:
            print(num,end=" ")
            num -= 1
        elif j >= end:
            print(num, end=" ")
            num +=1
        else:
            print(num, end=" ")
    print()
    if i < mid:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1 
