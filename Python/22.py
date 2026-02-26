# a = 'aabcdbcabd'
# print({'a':a.count('a'),'b':a.count('b'),'c':a.count('c'),'d':a.count('d')})

data = input("Enter a str: ")
i = 0
out = {}
while i < len(data):
    out[data[i]] = data.count(data[i])
    i+= 1
print(out)