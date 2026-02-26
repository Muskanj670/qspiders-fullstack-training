data = eval(input("Enter a list: "))
result = []
l = len(data)
i = 0
while (i < l):
    if type(data[i]) is int:
        if str(data[i]) == str(data[i])[::-1]:
            result.append(data[i])
    i += 1
print(result)
