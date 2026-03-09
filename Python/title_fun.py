# Title(): it is a inbuilt fun which is used to capitalize first letter after every space 

a = 'python is #vEry easy'
b = ["python",'is','very','easy']
print(a.title())
# print(b.title())
# print(" ".join(b.title()))

a = 'python is #vEry easy'
out = ''
for i in range(len(a)):
    if i == 0 or a[i-1] == ' ':
        out += a[i].upper()
    else:
        out += a[i].lower()
print(out)