class bank:    #Defining a class

    # Class properties
    bname = 'UBI'
    bloc = 'Agra'
    ceo = 'Muskan Jain'
    ifsc = 'UBIN0002'

    # Class Method to access class info
    @classmethod   # It is a decorator mandatory to create class method
    def bank_info(cls):  #cls is a mandatory and first argument which holds class address
        print(f'\nBank name : {cls.bname} \nBank location : {cls.bloc}\nBank CEO : {cls.ceo}\nIFSC : {cls.ifsc}\n')

    # Class method to update class properties
    @classmethod
    def change_location(cls):
        cls.bloc = cls.get_address()  #Getting new address from static method
        bank.bank_info()


    # Constructor to define object properties
    def __init__(self,name,ph,email,address):
        self.name = name
        self.ph = ph
        self.email = email
        self.address = address

    # Instance method to access object properties
    def customer_info(self):   #self is a mandatory and first argument which holds current object address
        print(f'\nAccount Holder Name: {self.name} \nPhone No: {self.ph} \nEmail: {self.email}\nAddress: {self.address}\n')

    # Instance method to modify object properties
    def change_customer_address(self):
        self.address = self.get_address()  #Getting new address from static method
        print(f'\n----------------Address Updated Successfully...........')
        self.customer_info()

    #Static method 
    @staticmethod  #Decorator used for creating static method
    def get_address():
        addr = input("Enter new address: ")
        return addr


# Calling class method to access class properties
bank.bank_info()

# Calling class methods to modify class properties
bank.change_location()

# Creating object and calling constructor to assign object properties
c1 = bank("Muskan Jain",7894561230,'muskan@gmail.com','Agra')

# Calling instance method to access object properties
c1.customer_info()

# Calling instance method to modify object property
c1.change_customer_address()

