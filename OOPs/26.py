# Example - 1
def instagram(func):
    def wrapper(*args,**kwargs):
        print("\nGo to www.instagram.com")
        print("Login")
        func(*args,**kwargs)
        print("Logout\n")

    return wrapper

# Example - 2 
import time
def total_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f'Total Time = {time.time() - start}\n')
    return wrapper

@total_time
@instagram
def Muskan_insta():
    print("Chat with bff ")

@total_time
def Snigdha_insta():
    print("Watches trainers stories")

def Nipurnika_insta():
    print("Watches Reels")

@instagram
def Amrita_insta():
    print("Chat with ______")

Muskan_insta()      #* Function with multiple decorator
Snigdha_insta()     #* Function with total_time decorator
Nipurnika_insta()   #* Function with no decorator
Amrita_insta()      #* Function with instagram decorator



