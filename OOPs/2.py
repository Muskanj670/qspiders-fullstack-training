class zoo:
    a = 'Alligator'
    b = 'Bear'
    c = 'Chimpanzee'

amrita = zoo()
snigdha = zoo()
deepak = zoo()
muskan = zoo()
print(zoo.a,zoo.b,zoo.c)
print(deepak.a,deepak.b,deepak.c)
print(amrita.a,amrita.b,amrita.c)
print(snigdha.a,snigdha.b,snigdha.c)
print(muskan.a,muskan.b,muskan.c)

zoo.c = 'Crocodile'

print(zoo.a,zoo.b,zoo.c)
print(deepak.a,deepak.b,deepak.c)
print(amrita.a,amrita.b,amrita.c)
print(snigdha.a,snigdha.b,snigdha.c)
print(muskan.a,muskan.b,muskan.c)

amrita.a = 'Panda'
deepak.a = 'Amrita'
snigdha.b = 'Racoon'
muskan.c = 'Penguin'

print(zoo.a,zoo.b,zoo.c)
print(deepak.a,deepak.b,deepak.c)
print(amrita.a,amrita.b,amrita.c)
print(snigdha.a,snigdha.b,snigdha.c)
print(muskan.a,muskan.b,muskan.c)