n = int(input("Enter a num: "))
start = 1
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="\t")
    pattern = start
    for j in range((i*2)-1):
        print(pattern,end="\t")
        if j < i-1:
            pattern +=1
        else:
            pattern -=1
        if j < i:
            start += 1
    print()