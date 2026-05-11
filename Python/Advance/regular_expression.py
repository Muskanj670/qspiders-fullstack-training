"""
! Regular Expression:
    - It is a concept by the help of which we can search and match pattern in a string by using some expression.
    - The module "re" is used for using regular expression.
    - Some important methods are:
        -> search(): matches from the string.
        -> match(): matches from the starting of the string.
        -> sub(): replaces the old substring with new one.
        -> findall(): Returns a list of all the matching patterns.
"""

import re
s = "The python programming language"
res = re.search("python", s)
print(res)
res = re.match("python", s)
print(res)
s = "python is a programming lang. Python is used in various domain"
res = re.match("python", s)
print(res)

# re.sub("old_str", "new_str", string, count = no)
res = re.sub("python",'react', s, count = 1)
print(res)

# ? '.' ----> matches any character
s = 'cut cat cup caac cap coat'
print(re.findall('c.t', s))
print(re.findall('c..t', s))

# ? '^' ----> matches the staring character
print(re.findall("^cut", s))
print(re.findall("^cat", s))

# ? "$" ----> matches at the end of the string
print(re.findall("coat$", s))
print(re.findall("cat$", s))

# ? "*" -----> Matches 0 or n chararters
print(re.findall("ca*", s))

# ? "+" ---> matches one or more characters
s = 'hello loo l'
print(re.findall("lo+", s))

# ? "?" ---> matches one or 0 characters
s = "color colour"
print(re.findall("colou?r", s))

# ? "\d" ----> Matches digit character
s = "muskanj8642@gmail.com"
print(re.findall("\d",s))

# ? "\D" ----> Matches non digit character
print(re.findall("\D",s))

# ? "{n}" ----> Matches exactly n no. of characters
s = '12 123 4123 345677'
print(re.findall("\d{4}", s))

# ? "{n,m}" ----> Matches exactly n to m no. of characters
print(re.findall("\d{3,6}", s))

# ? "[abc]" ---> Any one of a, b or c
s = "Hello123@"
print(re.findall("[aeiou]",s))

# ? "[^abc]" ----> not of a, b and c
print(re.findall("[^aeiou]",s))

# ? "[a-z]" ---> Range
print(re.findall("[a-z]",s))

# ? "[A-Z]" ---> Range
print(re.findall("[A-Z]",s))

# ? "[A-Za-z]" ---> Range
print(re.findall("[A-Za-z]",s))

# ? "[A-Za-z0-9]" ---> Range
print(re.findall("[A-Za-z0-9]",s))

# ? "\w" ---> Alphanum
print(re.findall("\w",s))

# ? "\W" ---> not Alphanum
print(re.findall("\W",s))

# ? "\w" ---> Alphanum
print(re.findall("\w",s))

# ? "\s" ---> SPACE
s = "Muskan is great!"
print(re.findall("\s",s))

# ? "\S" ---> not SPACE
print(re.findall("\S",s))

# ? "\b" ---> space arround
s = 'The cap is capital'
print(re.findall(r"cap",s))
print(re.findall(r"cap\b",s))

# ? "\." ----> Literal dot(Ignore special meaning of the character)
s = 'www.python.org'
print(re.findall(r'.',s))
print(re.findall(r"\.",s))


# ? "|" ---> or
s = 'cat cow dog ox'
print(re.findall("cat | dog", s))


# ! Replace the number with *
password = 'qsp2026'
res = re.sub("\d",'*', password)
print(res)



# Fetch all mobile no. from a string
# Fetch all the dates from a string
# Fetch all the valid pan card no
# fetch all the valid vehicle no from a given string
# Fetch all the email from a string




