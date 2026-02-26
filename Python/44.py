# for i in range(1,10,2):
#     for j in range(2,7,3):
#         print(i,j,end=" ")
#     print()

a = "How are you all"
a = a .split()
out = []
for i in a:
    c = 0
    for j in i:
        if j.lower() in "aeiou":
            c += 1
    out.append(c)
print(out)

out = []
for i in range(1,11):
    fact = 1
    for j in range(1,i+1):
        fact *= j 
    out.append(fact)
print(out)


a = [10,"hello",3+5j,321]
out = []
for i in a:
    if type(i) == int:
        c = 0
        for j in str(i):
            c += int(j)
        out.append(c)
print(out)


a = "Kabab is love".split()
out = {}
for i in a:
    c = 0
    for j in range(len(i)):
        if i[j].lower() in "aeiou":
            c += 1
    out[i] = [i[::-1],c,i[::2]]
print(out)

out = {}
for i in a:
    c = 0
    c2 = ''
    for j in i:
        if j.lower() not in "aeiou":
            c += 1
            c2 += j
    out[i[0]+i[-1]] = [c2[::-1],c,c2]

print(out)
