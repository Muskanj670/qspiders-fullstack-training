a = "BUIGYGHfufuhUHIUGh"
for i in a:
    if not 'A' <= i <= 'Z':
        continue
    print(i, end=" ")

print("\n")

a = [1.1,"hii",221,121,1221]
for i in range(len(a)):
    if i%2 !=0 or type(a[i]) != int or str(a[i]) != str(a[i])[::-1]:
        continue
    print(a[i], end=' ')

print("\n")

                          