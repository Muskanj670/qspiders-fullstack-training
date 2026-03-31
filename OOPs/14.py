# Hybrid Inheritance

class upper:
    @staticmethod
    def upper():
        upp = ''
        for i in range(ord('A'), ord('Z')+1):
            upp += chr(i)
        print(upp)

class Alpha(upper):
    @staticmethod
    def lower():
        low = ''
        for i in range(ord('a'), ord('z')+1):
            low += chr(i)
        print(low)

class Numbers:
    @staticmethod
    def numbers():
        num = ''
        for i in range(10):
            num += str(i)
        print(num)

class characters(Alpha,Numbers):
    @staticmethod
    def special():
        sp = ''
        for i in range(32,128):
            if not chr(i).isalnum():
                sp += chr(i)
        print(sp)

obj = characters()
obj.upper()
obj.lower()
obj.numbers()
obj.special()
