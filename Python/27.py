data = input("Enter a str: ")
i = 0
res = ''
while i < len(data):
    if data[i] not in res:
        res +=data[i] + str(data.count(data[i]))
    i+= 1
print(res)
