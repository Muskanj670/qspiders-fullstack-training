n = int(input("Enter a number: "))
space = n - 1
patternSize = 1
for i in range(1, n+1):
    print("  "*space + "* "*patternSize + "  "*((2*space)+1) + "* "*patternSize + "  "*((2*space)+1)+ "* "*patternSize)
    patternSize += 2
    space -= 1
        