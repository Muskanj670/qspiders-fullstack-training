# Has-a Relationship
# !Aggregation

class Address:
    def __init__(self,state,city,pin):
        self.state = state
        self.city = city
        self.pin = pin

add1= Address('UP','Noida',200100)

class Customer:
    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr

c1= Customer("Rahul",22,add1)

print(c1.name)
print(c1.age)
print(c1.addr.state)
print(c1.addr.city)
print(c1.addr.pin)

# !Composition

class Address:
    def __init__(self,state,city,pin):
        self.state = state
        self.city = city
        self.pin = pin

class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.addr = Address('UP','Noida',200100)

c1= Customer("Rahul",22)

print(c1.name)
print(c1.age)
print(c1.addr.state)
print(c1.addr.city)
print(c1.addr.pin)
         