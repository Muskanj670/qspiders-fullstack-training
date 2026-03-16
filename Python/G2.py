def f_extractInt(a):
    out = []
    for i in a :
        if type(i) is int:
            out += [i]
    return out

print(list(f_extractInt([12,2,3,3.4,'hello'])))

def g_extractInt(a):
    for i in a :
        if type(i) is int:
            yield i

print(list(g_extractInt([12,2,3,3.4,'hello'])))