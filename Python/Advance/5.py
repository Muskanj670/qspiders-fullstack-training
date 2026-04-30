"""
! Functional Programming:
    * Anonymous Function:
        - These are the functions which don't have any name, those are defined with the help of lambda keyword, Also known as lambda expression. 
        - It also known as single line function.
        - We can pass n no. of arguments and get single output.
        - For simple mathematical operations lambda function is used.
        - Simple if-else program can be solved.
"""

def lambda_fun():
    Sum = lambda a, b: a + b
    print(Sum(2,3))

    calc = lambda *args : sum(args)
    print(calc(1,2,3,4))

    reverse = lambda num : int(str(num)[::-1])
    print(reverse(2345))

    square = lambda num : num*num
    print(square(2))

    float_val = lambda num : int(str(num).split(".")[-1])
    print(float_val(1234.34567))

    is_equal = lambda num1, num2 : num1 == num2
    print(is_equal(10,20))
    print(is_equal(20,20))

    is_equal = lambda a, b: "Equal" if a == b else "Not Equal"
    print(is_equal(10,20)) 

    is_odd = lambda num: num % 2 != 0
    print(is_odd(3))

    is_evan = lambda num: num % 2 == 0
    print(is_evan(3))

    is_palindrome = lambda num : num == int(str(num)[::-1])
    print(is_palindrome(232))
    print(is_palindrome(2323)) 

    is_positive = lambda num : num >= 0
    print(is_positive(234567))

    is_negative = lambda num: num < 0
    print(is_negative(-2345))

    is_single_digit = lambda num: 1 == len(str(num))
    print(is_single_digit(34))

# Nested lambda

def nested_lambda():
    func = lambda a: lambda b: a+b
    print(func(10)(20))


    add_5 = func(5)
    add_15 = func(15)
    add_25 = func(25)

    print(add_5(100))
    print(add_15(100))
    print(add_25(100))

# nested_lambda()

"""
    * map() :
        - It is used to traverse through the collection and apply same task to each and every value of the collection.
        - The length of input will be same as length of output.
        - It is used to process and modify the collection.
        - It takes 2 arguments :
            -> Function
            -> Iterable/ collection
        ? Syntax:
            var = map(func_name, iterable)
            print(list(var))

        - map function returns map object, Hence type casting is required. 
"""
def map_examples():
    l1 = [1,2,3,4,5] 
    def multiply_10(n):
        return n*10
    var = map(multiply_10, l1)
    print(list(var))

    Sum_10 = lambda n: n + 10
    print(list(map(Sum_10, l1)))
    
    # ! Single line code
    # print(list(map(lambda n : n*10, eval(input("Enter a list: ")))))

    print(list(map(lambda s : ord(s), 'abc')))
    
    # ! Using in-built function
    print(list(map(ord, 'abcdef')))

    print(list(map(len, input("Enter a string: ").split())))

    s = '10 20 30 40'
    print(list(map(int, s.split())))

    s = 'This is a string'
    print(dict(zip(s.split(),list(map(len, s.split())))))
    print(dict(map(lambda word : (word, len(word)), s.split())))

    l1 = [11,2,543,89,1]
    def digit_sum(n):
        n = str(n)
        Sum = 0
        for i in n:
            Sum += int(i)
        return Sum

    print(list(map(digit_sum, l1)))
    print(list(map(lambda n: sum([int(i) for i in str(n)]), l1 )))




map_examples()
"""

    * filter() :
    * reduce
"""