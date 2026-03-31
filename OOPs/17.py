'''
!Method Chaining in Python
It is a process of calling multiple methods by using single object in a single line of code. It is also known as fluent interface. It is used to improve the readability of the code.
Syntax:
object.method1().method2().method3()...

In order to achieve method chaining each method should return self inside the class.
'''

class person:
    def __init__(self):
        self.name = None
        self.age = None

    def create_name(self,name):
        self.name = name
        return self

    def create_age(self,age):
        self.age = age
        return self

    def show(self):
        print(f'Name = {self.name} \nage = {self.age}')
        # return self

obj = person()
obj.create_name("Muskan").create_age(22).show()