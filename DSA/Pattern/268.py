n = int(input("Enter a number: "))
mid = n//2 + 1
space = mid - 1
patternSize = 1
for i in range(1, n+1):
    if i <= mid:
        print("  "*space + "* "*patternSize + "  "*((2*space)+1) + "* "*patternSize + "  "*((2*space)+1)+ "* "*patternSize)
    else:
        print("  "*(mid-1) + "* " +"  "*((mid-1)*2 +1) + "* " +"  "*((mid-1)*2 +1) + "* " )
    patternSize += 2
    space -= 1
        