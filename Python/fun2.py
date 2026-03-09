def fun(l):
    out = {}
    for i in l:
        if type(i) in [list,tuple,dict, set,str]:
            out[i] = len(i)
        else:
            out[i] = 1

    print(out)

fun(["hai",3+5j,(1,2),98,'apple'])
