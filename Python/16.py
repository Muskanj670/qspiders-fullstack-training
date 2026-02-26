print("Create your account...........")
id = eval(input("enter id : "))
pwd = eval(input("Enter pwd: "))
cpwd = eval(input("Enter pwd again: "))

if pwd == cpwd:
    print("Id created..")
    id_ = eval(input("enter id : "))
    pwd_ = eval(input("Enter pwd: ")) 

    if id == id_ and pwd == pwd_:
        print("Logged in.")
    else:
        print("Invalid id pwd")
else:
    print("Pwd not confirmed")