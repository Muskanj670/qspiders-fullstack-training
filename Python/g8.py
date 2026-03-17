a = eval(input("Enter a list: "))
def isPalindrome(a):
    for i in a:
        if type(i) == int and str(i) == str(i)[::-1]:
            yield (i, len(str(i)))

print(list(isPalindrome(a)))