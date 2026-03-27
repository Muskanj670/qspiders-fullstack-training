# Multi Level Inheritance

class parent:
    a = 10
    b = 20
    def show_parent(self):
        print("Hello from Demo class")
    
class child(parent):
    c = 30
    d = 40
    def show_child(self):
        print("Hello from Child class")

class grand_child(child):
    e = 50
    f = 60
    def show_grand_Child(self):
        print("Hello from Grand Child class")

obj = grand_child()
print(obj.a)
print(obj.b)
obj.show_parent()
print(obj.c)
print(obj.d)
obj.show_child()
print(obj.e)
print(obj.f)
obj.show_grand_Child()