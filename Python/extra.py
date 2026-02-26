a = int(input("Enter a number: "))
result = 0
temp = a
while (a > 0):
    rem = a % 10
    result += rem**3
    a //= 10
if (result == temp):
    print('Yes')
