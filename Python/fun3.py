def example():
    return 1,2,3
a,b,c = example()
print(a,b,c)



def caps():
    a = 'PyThOn'
    out = ''
    for i in a:
        if i == i.upper():
            out += i 

    return out
print(caps())

def dic():
    a = "python is Programming language".split()
    out = {}
    for i in a:
        if i[0].lower() not in out:
            out[i[0].lower()] = [i]
        else:
            out[i[0].lower()].append(i)

    return out
print(dic())


def highest_number():
    num = [1,2,3,65,32,345,7562]
    highest = 0
    smallest = float('inf')
    for i in num:
        if i > highest:
            highest = i
        if i < smallest:
            smallest = i
    return highest , smallest
print(highest_number())