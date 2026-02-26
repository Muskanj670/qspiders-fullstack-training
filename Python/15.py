data = eval(input("Enter The data: "))
if data in [str,list,tuple,set,dict]:
    if len(data) > 3:
        print (data)
    else:
        print('Multivalue Data')
else:
    print("Single vale data")