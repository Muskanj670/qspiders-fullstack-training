# Encapsulation


class Bank:
    def __init__(self,name,addr,pin,bal):
        self.name = name
        self.addr = addr
        self.__pin = pin
        self.__bal = bal

    def get_bal(self):
        pin = int(input("Enter pin: "))
        if pin == self.__pin:
            print("Current bal is ",self.__bal)

    def deposit(self):
        pin = int(input("Enter pin: "))
        if pin == self.__pin:
            amt = int(input("Enter amt to deposit: "))
            self.__bal += amt
            print("Deposit successful. Current bal is ",self.__bal)

    def change_pin(self):
        pin = int(input("Enter old Pin: "))
        if pin == self.__pin:
            new_pin = int(input("Enter new pin: "))
            self.__pin = new_pin
            print(f'Pin updated successfully. New pin is {self.__pin}')

obj = Bank("Muskan","Agra",2003,10000)
obj.get_bal()
obj.deposit()
obj.change_pin()