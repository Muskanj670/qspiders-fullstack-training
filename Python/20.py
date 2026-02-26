a = input("Enter a string: ")
i = 0
j = 0
length = len(a)
out = ''
while i < length:
    if 'A' <= a[i] <= 'Z':
        out+= a[i]
    i += 1
print(out+str(len(out)))

out = ''

while j < length:
    if a[j] in 'aeiouAEIOU':
        out += a[j]
    j += 1
print ('\n',out, len(out))
