# for i in range(1,101):
#     if i%3 == 0 and i %5 == 0:
#         print (i, end=" ")


# sum = 0
# for i in "hello":
#     sum += 1
# print(sum)


# for i in "HelloWorld":
#     if 'A' <= i <= 'Z':
#         print(i, end=" ")


# mail = "muskanj8642@gmail.com"
# sum = 0
# for i in mail:
#     if '0' <= i <= '9':
#         sum += int(i)
# print(sum)


# a= [1,'world',4,2,5,3.4,4,2,7,4,'hello']
# for i in range(0,len(a),2):
#     if type(a[i]) == int and a[i] % 2 == 0:
#         print (a[i], end=" ")


# a = 'HeHloWorld'
# out = ''
# res = {}
# for i in range (0,len(a),2):
#     if 'A' <= a[i] <= 'Z' and ord(a[i]) % 3 == 0:
#         out += a[i]

# for i in out:
#     res[i] = out.count(i)
# print(res)


a ='ava nitin good ata'
out = ''
a = a.split()
for i in range(len(a)):
    if a[i] == a[i][::-1]:
        out+=a[i]+' '

print(out)