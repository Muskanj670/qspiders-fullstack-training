input = ['amazon.com','jio cinema.com','python.py','index.html']
out = {}
for i in input:
    i = i.split('.')
    if i[1] not in out:
        out[i[1]] = [i[0]]
    else:
        out[i[1]] += [i[0]]
print(out)