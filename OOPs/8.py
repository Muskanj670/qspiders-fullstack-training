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

    @staticmethod
    def get_amount():
        amount = int(input("Enter amount: "))
        return amount

# Creating object and calling constructor to assign object properties
c1 = bank("Muskan Jain",7894561230,'muskan@gmail.com','Agra',10000)
c1.customer_info()
c1.deposit()
c1.withdraw()

