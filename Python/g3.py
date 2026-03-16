def isPalindrome(a):
    return str(a) == str(a)[::-1]

def g_extractPalindromeInt(a):
    for i in a:
        if type(i) is int and isPalindrome(i):
            yield i

print(list(g_extractPalindromeInt([34,53,33,2,4.4,'hello'])))