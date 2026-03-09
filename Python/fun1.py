def up():
    a = 'AjrgrhSNF'
    OUT = ""
    for char in a:
        if char.isupper():
            OUT += char
    print(OUT)
up()


def firstup():
    a = "python"
    out = ''
    for i in a:
        if i == a[0]:
            out += chr(ord(i)-32)
        else:
            out += i
    print(out)
firstup()


def convert():
    a = "010$01!001~0"
    out = ''
    for i in a:
        if i == '0':
            out += '1'
        elif i == '1':
            out += '0'
        else:
            out += '#'

    print(out)
convert()