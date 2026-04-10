def reverseList(a,start, end):
    if end >= len(a):
        return "List index out of range"
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

    return a

a = eval(input("Enter a list: "))
start = int(input("Enter Starting Index: "))
end = int(input("Enter ending Index: "))

print(reverseList(a,start,end))

