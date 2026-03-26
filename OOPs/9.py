class bank:   
    bname = 'UBI'
    bloc = 'Agra'
    ceo = 'Muskan Jain'
    ifsc = 'UBIN0002'

    def __init__(self,name,ph,email,address,bal):
        self.name = name
        self.ph = ph
        self.email = email
        self.address = address
        self.balance = bal

    # Instance method to access object properties
    def customer_info(self):  
        print(f'\nAccount Holder Name: {self.name} \nPhone No: {self.ph} \nEmail: {self.email}\nAddress: {self.address}\nBalance: {self.balance}\n')

    # Instance method to modify object properties
    def deposit(self):
        self.balance = self.balance + self.get_amount()
        print("\n...........Amount Deposited successfully........\n")
        print(f'Current Balance : {self.balance}\n')
        
    def withdraw(self):
        sub = self.get_amount()
        if self.balance < sub:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - sub
            print("...........Amount Withdrawal successfully........")
        print(f'Current Balance : {self.balance}\n')

    @classmethod   # It is a decorator mandatory to create class method
    def bank_info(cls):  #cls is a mandatory and first argument which holds class address
        print(f'\nBank name : {cls.bname} \nBank location : {cls.bloc}\nBank CEO : {cls.ceo}\nIFSC : {cls.ifsc}\n')

    @classmethod
    def change_location(cls):
        cls.bloc = cls.get_address()  #Getting new address from static method
        bank.bank_info()

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

    @staticmethod
    def get_amount():
        amount = int(input("Enter amount: "))
        return amount

# Creating object and calling constructor to assign object properties
c1 = bank("Muskan Jain",7894561230,'muskan@gmail.com','Agra',10000)
dic = {'c1':c1}
obj = input("Enter customer name: ")
if obj not in dic:
    print("No customer available with name "+obj)
    print(f'Please select from {dic.keys()} ')

else:
    customer = dic[obj]
    while True:
        print("\n1. Customer Info \n2. Deposit Amount : \n3. Withdraw Amount \n4. Bank Info \n5. Change Customer Address \n6. Change Bank Address \n7/ Exit \n\n")
        choice = int(input("Enter Your Choice...."))

        if choice == 1:
            customer.customer_info()
        elif choice == 2:
            customer.deposit()
        elif choice == 3:
            customer.withdraw()
        elif choice == 4:
            bank.bank_info()
        elif choice == 5:
            customer.change_customer_address()
        elif choice == 6:
            bank.change_location()
        elif choice == 7:
            print("..............Exit..................")
            break
        else:
            print("Invalid Input")

