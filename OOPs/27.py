# ------------------------------Example - 1 -----------------------------------------------
def monitor_execution(func):
    def wrapper(*args,**kwargs):
        print("Execution is started")
        print(f"Result is {func(*args)}")
        print("Execution is completed")
    return wrapper

@monitor_execution
def add(*args):
    return sum(args)

add(2,3,4)


# ------------------------------Example - 2 -----------------------------------------------
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if i < 0:
                print("Negative value detected")
                return
        func(*args,**kwargs)
    return wrapper

@validate_positive
def add(*args):
    print(f"Sum is {sum(args)}")

add(2,3)
add(2,-3)


@validate_positive
def age(age):
    print("Data stored successfully")

age(22)
age(-22)

# ------------------------------Example - 3 -----------------------------------------------

def login_required(func):
    def wrapper(*args,**kwargs):
        is_logged_in = eval(input("Do you want to log in (True/False): "))
        if is_logged_in:
            func(*args, **kwargs)
        else:
            print("Log in required")
    return wrapper

@login_required
def delete_data():
    print("Data deleted")

delete_data()