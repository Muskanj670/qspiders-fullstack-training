# Single Level Inheritance

class parent:
    a = 10
    b = 20
    def show(self):
        print("Hello from Demo class")
    
class child(parent):
    pass

obj = child()
print(obj.a)
print(obj.b)
obj.show()