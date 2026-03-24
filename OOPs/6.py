class bank:
    @classmethod
    def bank_info(cls):
        print(f'\nBank name : {cls.bname} \nBank location : {cls.bloc}\nBank CEO : {cls.ceo}\n')

    @classmethod
    def change_location(cls):
        new = input(f"Enter new location : ")
        cls.bloc = new
        bank.bank_info()

    bname = 'UBI'
    bloc = 'Agra'
    ceo = 'Muskan Jain'

    def __init__(self,name,ph,email):
        self.name = name
        self.ph = ph
        self.email = email

bank.bank_info()
bank.change_location()
c1 = bank("Muskan Jain",7894561230,'muskan@gmail.com')
print(c1.name)
c2 = bank("Amrita Singh",7894561230,'amrita@gmail.com')
print(c2.name, c2.ph)
c3 = bank('Nipunika',7418529630,'nipunika@gmail.com')
print(c3.email)
