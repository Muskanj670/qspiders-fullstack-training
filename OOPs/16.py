# -------------------
# !Constructor Chaining
# -------------------
# It is the Process of invoking(calling) parent class constructor inside the child class constructor
# It can be done using two ways:
# ?1. Constructor Chaining using Super() function

class bank:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class SBI(bank):
    def __init__(self,name,age,email,ph,addr):
        super().__init__(name,age)
        self.email = email
        self.ph = ph
        self.address = addr

obj = SBI("Muskan",22,'muskan@gmail.com',789461230,'Noida')
print(obj.name)
print(obj.age)
print(obj.email)
print(obj.ph)
print(obj.address)

# -----------------------------------------------
# ?2. Constructor Chaining using class name
# -----------------------------------------------

class A:
    def __init__(self):
        print("Constructor of class A")

class B:
    def __init__(self):
        print("Constructor of class B")

class C:
    def __init__(self):
        print("Constructor of class C")

class D(A,B,C):
    def __init__(self):
        B.__init__(self)
        super().__init__()

obj = D()