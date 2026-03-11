cp = int(input("Enter a CP: "))
sp = int(input("Enter a SP: "))
if sp > cp:
    print(((sp-cp)/cp)*100 ,"% Profit")
else:
    print(((cp-sp)/cp)*100,"% Loss")