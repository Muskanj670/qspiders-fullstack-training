a = int(input("Enter a num: "))
for i in range(a+1):
    print('*'*i)
print()

for i in range(a,0,-1):
    print('*'*i)
print()

for i in range(a,0,-1):
    print(' '*i+"*"*(a-i+1)+"*"*(a-i))

for i in range(a+1):
    print(' '*(i+1)+'*'*(a-i)+'*'*(a-i-1))

print()

for i in range(a+1,0,-1):
    print('*'*i+" "*(a-i+1)+" "*(a-i)+'*'*i)

for i in range(a+1):
    print('*'*(i+1)+' '*(a-i)+' '*(a-i-1)+'*'*(i+1))
    
    