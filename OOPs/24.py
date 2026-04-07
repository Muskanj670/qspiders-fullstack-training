class person:
    def __init__(self,name,pin,email):
        self.name = name
        self.__pin = pin
        self.__email = email

    @property
    def person_name(self):
        return self.name

    @property
    def pin(self):
        return self.__pin

    @property
    def email(self):
        print(self.__email)

    @email.setter
    def email(self, email):
        self.__email = email
        print(f"Email updated to {self.__email}")

    @email.deleter
    def email(self):
        print(f"Email {self.__email} deleted")
        del self.__email

obj = person("Muskan",1234,"muskan@example.com")
print(obj.person_name)
print(obj.pin)
obj.email
obj.email = "new@example.com"
del obj.email