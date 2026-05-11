num1 = eval(input("Enter a data: "))
num2 = eval(input("Enter a data: "))

try:
    def divide(num1, num2):
        print(num1/num2)
    # divide(num1, num2)
except TypeError:
    print("Provide a valid data type for division...")
except ZeroDivisionError:
    print("Num 2 can't be zero...")
else:
    print("qwertyu")
finally:
    print("End of code.")

"""
! Generic Exception Hnadling
    - When we don't know the exact type of exception.
    Exception   -> Base class for all the exception except keyboardInterrupt
                -> Hence we can not handle keyBoardInterrupt
"""

try:
    def div(a , b):
        print(a/b)
    # div(num1, num2)
except Exception:
    print("Something went wrong")
else:
    print("Good to go!")
finally:
    print("This is the end...")

"""
! Default exception handling
    - By the help of it we can handle all the exceptions including KeyBoardInterrupt.
"""

def infinite_loop():
    i = 1
    while True:
        print(i)
        i+= 1

try:
    def div(a , b):
        print(a/b)
    # div(num1, num2)
    # infinite_loop()
except TypeError:
    print("Incorrect Data Type..")
except Exception:
    print("Something went Wrong")
except:
    print("keyBoardInterrupt")
else:
    print("Every thing is good..")
finally:
    print("End of code..")


"""
! Custom Exception
    - By the help of raise keyboard we can throw error at the any point of the program.
"""

def validate_age():
    age = int(input("Enter a number: "))
    if age < 18:
        raise ValueError("Age can not be less than 18")
    else:
        print("PROCEED")

validate_age()

"""
! User defined Exception
    - We can define our own exception by extending Exception class.
"""
class MyException(Exception):
    def __init__(self, message):
        print(message)
class HDFC:
    def __init__(self, bal):
        self.bal = bal

    def withdraw(self):
        amount = int(input("Enter the amount: "))
        if amount < 0:
            raise MyException("Negative amount can not be withdrawn")
        
        if amount > self.bal:
            raise MyException("Insufficient Bal")
        
        else:
            self.bal -= amount

obj = HDFC(2000)
try:
    obj.withdraw()
except MyException:
    pass