# Multiple Inheritance

class add:
    @staticmethod
    def add(a,b):
        print(a+b)

    a = 10

class sub:
    @staticmethod
    def sub(a,b):
        print(a-b)
    
    a = 20

class mul:
    @staticmethod
    def mul(a,b):
        print(a*b)

    a = 30

class calculator(add,sub, mul):
    @staticmethod
    def div(a,b):
        print(a/b)

    a = 40

obj = calculator()
obj.add(10,20)
obj.sub(10,20)
obj.mul(10,20)
obj.div(10,20)
print(obj.a)