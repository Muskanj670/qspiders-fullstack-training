n = int(input("Enter a number: "))
patternSize = n
space = 0
mid = n //2 + 1

for i in range(1, n+1):
    if i < mid:
        print("  "*(mid-1) + "* "+"  "*((mid-1)*2+1) + "* "+"  "*((mid-1)*2 +1)+ "* ")
    else:
        print("  "*space +"* "*patternSize + "  "*(2*space+1) + "* "*patternSize + "  "*(2*space+1) +"* "*patternSize)
        space += 1
        patternSize -= 2