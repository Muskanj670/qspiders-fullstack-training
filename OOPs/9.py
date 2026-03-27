class bank:   
    bname = 'UBI'
    bloc = 'Agra'
    ceo = 'Muskan Jain'
    ifsc = 'UBIN0002'

    def __init__(self,name,ph,email,address,bal,pin):
        self.name = name
        self.ph = ph
        self.email = email
        self.address = address
        self.balance = bal
        self.pin = pin

    # Instance method to access object properties
    def customer_info(self):  
        print(f'\nAccount Holder Name: {self.name} \nPhone No: {self.ph} \nEmail: {self.email}\nAddress: {self.address}\nBalance: {self.balance}\nPin: {self.pin}')

    # Instance method to modify object properties
    def deposit(self):
        self.balance = self.balance + self.get_amount()
        print("\n...........Amount Deposited successfully........\n")
        print(f'Current Balance : {self.balance}\n')
        
    def withdraw(self):
        if self.pin == self.get_pin():
            sub = self.get_amount()
            if self.balance < sub:
                print("Insufficient Balance")
            else:
                self.balance = self.balance - sub
                print("...........Amount Withdrawal successfully........")
            print(f'Current Balance : {self.balance}\n')
        else:
            print("Entered Incorrect password .......")
        
        # Instance method to modify object properties
    def change_customer_address(self):
        if self.pin == self.get_pin():
            self.address = self.get_address()  #Getting new address from static method
            print(f'\n----------------Address Updated Successfully...........')
            self.customer_info()
        else:
            print("-------Incorrect Password-------")

    def change_customer_pin(self):
        if self.pin == self.get_pin():
            pin = input("\nEnter New pin: ")
            self.pin = pin
            print("Pin Changed Successfully.......")
        else:
            print("........Incorrect pin..........")

    @classmethod   # It is a decorator mandatory to create class method
    def bank_info(cls):  #cls is a mandatory and first argument which holds class address
        print(f'\nBank name : {cls.bname} \nBank location : {cls.bloc}\nBank CEO : {cls.ceo}\nIFSC : {cls.ifsc}\n')

    @classmethod
    def change_location(cls):
        cls.bloc = cls.get_address()  #Getting new address from static method
        bank.bank_info()

    #Static method 
    @staticmethod  #Decorator used for creating static method
    def get_address():
        addr = input("Enter new address: ")
        return addr

    @staticmethod
    def get_amount():
        amount = int(input("Enter amount: "))
        return amount
    
    @staticmethod
    def get_pin():
        pin = input("\nEnter your Password :")
        return pin

def create_customer():
        name = input("Enter Name: ")
        ph = int(input("Enter Phone: "))
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        bal = int(input("Enter Initial Balance: "))
        pin = input("Set PIN: ")

        customer = bank(name, ph, email, address, bal, pin)
        return customer

dic = {}
while True:
    print("1. Create Customer\n2.View Customer\n3. Exit\n\n")
    main_choice = int(input("Enter Your Choice: "))
    if main_choice == 1:
        key = f'c{len(dic)+1}'
        dic[key] = create_customer()
        print(f"Customer created with ID: {key}")
    elif main_choice == 2:
        obj = input("Enter customer name: ")
        if obj not in dic:
            print("No customer available with name "+obj)
            print(f'Please select from {list(dic.keys())} ')

        else:
            customer = dic[obj]
            while True:
                print("\n1. Customer Info \n2. Deposit Amount \n3. Withdraw Amount \n4. Bank Info \n5. Change Customer Address \n6. Change Bank Address \n7. Change Customer Pin \n8. Exit \n\n")
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
                    customer.change_customer_pin()
                elif choice == 8:
                    print("..............Exit..................")
                    break
                else:
                    print("Invalid Input")

    elif main_choice == 3:
        print("\n\t\t\t....Exit .....")
        break
    else:
        print("\n\nIncorrect Input")

