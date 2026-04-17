"""
! Generator :
    - Simpler way of creating the iterator.
    - It is a function which uses yield keyword to generate item one at a time(instead of storing all value in the memory).
    - Yield keyword pause the execution and return the value.
    - Generator function return generator object which is iterable object to get the value we can perform looping on it. 

! Difference Between yield and return
"""

def naturalNumber(stop):
    for i in range(1,stop):
        yield i
print(list(naturalNumber(10)))

def evenNumber(stop):
    for i in range(stop):
        if i % 2 == 0:
            yield i
print(list(evenNumber(10)))

def fibonacci(stop):
    a = 0
    b = 1
    for i in range(stop):
        yield a
        a, b = b , a+b
print(list(fibonacci(10)))

def numberSquare(n):
    for i in range(1,n+1):
        yield i*i
print(list(numberSquare(1000000)))