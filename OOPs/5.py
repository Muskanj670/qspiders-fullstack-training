class bank:
    bname = 'UBI'
    bloc = 'Agra'
    ceo = 'Muskan Jain'

    def __init__(self,name,ph,email):
        self.name = name
        self.ph = ph
        self.email = email

c1 = bank("Muskan Jain",7894561230,'muskan@gmail.com')
print(c1.name)
c2 = bank("Amrita Singh",7894561230,'amrita@gmail.com')
print(c2.name, c2.ph)
c3 = bank('Nipunika',7418529630,'nipunika@gmail.com')
print(c3.email)
