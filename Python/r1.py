def getFactorial(num):
    if num < 2:
        return 1
    return num * getFactorial(num - 1)
print(getFactorial(5))

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

def getFactorial(num):
    if num < 2:
        return 1
    return num * getFactorial(num - 1)
print(getFactorial(1558))

    