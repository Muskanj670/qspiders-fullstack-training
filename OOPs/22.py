# Operator Overloading

class Arithmetic():
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self, other):
        return self.a*other.a
    def __mod__(self, other):
        return self.a%other.a

class myclass():
    def __init__(self,list1):
        self.list1=list1
    def __getitem__(self, key):            #updating by using indexing
        return self.list1[key]
    def __setitem__(self, key, value):      #implement the in operator
        self.list1[key]=value
    def __contains__(self, item):
        return item in self.list1
    def __delitem__(self, key):
        del self.list1[key]
    
class student():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __str__(self):
        return f"Name is {self.name},rollno is {self.roll}"
    def __repr__(self):
        return f"student({self.name},{self.roll})"
    
obj1=Arithmetic(40)
obj2=Arithmetic(20)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1%obj2)

newobj=myclass([10,20,30])
print(newobj[-1])
newobj[-1]=300
print(newobj.list1)
del newobj[0]
print(20 in newobj)
print(newobj.list1)

s1=student("amrita",7)
print(str(s1))