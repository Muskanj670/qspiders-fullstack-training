# Duck Typing

def sum(a,b):
    print(a+b)

class Integer:
    def add(self,a,b):
        sum(a,b)

class Float:
    def add(self,a,b):
        sum(a,b)

class Character:
    def add(self,a,b):
        sum(a,b)

a = Integer()
b = Float()
c = Character()

a.add(2,3)
b.add(2.3, 4.5)
c.add("hello ","world")