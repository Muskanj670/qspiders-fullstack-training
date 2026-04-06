# ! Method overloading
"""
        ! Using default arguments
"""
class Demo:
    def add(self,a,b,c = 0):
        print(a+b)
obj = Demo()
obj.add(10,20,30)

"""
        ! Using Variable length arguments arguments
"""
class Demo2:
    def add(self,*args):
        print(sum(args))

obj1 = Demo2()
obj1.add(10,20)
obj1.add(10,20,30)
obj1.add(10,20,30,40)