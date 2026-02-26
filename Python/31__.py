a = input("Enter you str: ")
i = 0
res = ""
count = 1

# while i < len(a):
#     if i == len(a) -1:
#         if a[i] == a[i-1]:
#             res += a[i] + str(count)
#         else:
#             res += a[i] + str(count)
#     elif a[i] == a[i+1]:
#         count += 1
#     else:
#         res += a[i] + str(count)
#         count = 1

#     i += 1

# print(res)

while i < len(a) -1:
    if a[i] == a[i+1]:
        count += 1
    else:
        res += a[i] + str(count)
        count = 1

    i += 1

res += a[-1] + str(count)
print(res)