num = input("Enter a number: ")
s1 = int(num[0]) + int(num[-1])
s2 = 0

for i in range (1,len(num)-1):
    s2+= int(num[i])

if s1 == s2:
    print("Xylem")
else:
    print("Pholem")

