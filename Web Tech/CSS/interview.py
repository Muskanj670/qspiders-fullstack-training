# n = int(input("Enter a num: "))
# j = n // 2
# initial = 1
# while j > 0:
#     for i in range(0+initial,2+initial):
#         print(i , i+2)
#     j -= 1
#     initial += 4

    
a = [10,20,30,40,50]
out = []
for i in range(len(a)-1,0,-1):
    out.append(a[i])
out.append(a[0])
print(out)