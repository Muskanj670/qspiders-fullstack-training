def calculator(op,op1,op2):
    if op == 1:
        return op1+op2
    elif op ==2:
        return op1-op2
    elif op ==3:
        return op1*op2
    elif op ==4:
        return op1/op2
    else:
        return "Invalid Value Entered"
    

print("""Select: 
      1. Addition 
      2. Subtract 
      3. Multiplication 
      4. Div""")
op = int(input("Enter a number (1-4):"))
op1= int(input("Enter values: "))
op2 = int(input("Enter value: "))
print(calculator(op,op1,op2))
#   --------------------------------------------or----------------------------------------------


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
           
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")