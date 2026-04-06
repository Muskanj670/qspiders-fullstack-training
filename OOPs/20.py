# ! Method overriding

class parent:
    def show(self):
        print("Parent class")

class child(parent):
    def show(self):
       print("Child class")

obj = child()
obj.show() 

