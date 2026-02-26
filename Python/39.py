email = "muskanj670"
pwd = 12345678

while True:
    email_id = input("Enter an email :")
    pas = int(input("Enter your pword: "))
    if email == email_id and pwd == pas:
        print("Welcome....................")
        break
    else:
        print("Incorrect credential.....")