# a = eval(input("Enter a list: "))
# new = ''
# for i in a:
#     new+= str(i)
# res = str(int(new) + 1)
# out = []
# for i in res:
#     out.append(int(i))

# print(out)

b = eval(input("Enter a list: "))
def plus_one(lst):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] + 1 < 10:
            lst[i] += 1
            return lst
        lst[i] = 0
        if i == 0:
            return [1] + lst

print(plus_one(b))