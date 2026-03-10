def evenPositionLengthCounter(a):
    out = []
    for i in range(len(a)):
        if i % 2 != 0 and type(a[i]) in [str,tuple,list,dict,set]:
            out.append(len(a[i]))
        else:
            out.append(a[i])

    return out
print(evenPositionLengthCounter(['hello','ab',3.5,65,[1,2],'star',3+5j]))

# Anagram: These are the strings where we verify same length, same characters present inside the strings
def isAnagram(a,b):
    if len(a) != len(b):
        return False
    else:
        a_ = {}
        b_ = {}

        for i in a:
            if i not in a_:
                a_[i] = a.count(i)
        for i in b:
            if i not in b_:
                b_[i] = b.count(i)

        return True if a_ == b_ else False
    
print(isAnagram('silent','listen'))

# or

def isAnagram(a,b):
    return True if len(a) == len(b) and sorted(a) == sorted(b) else False   
print(isAnagram('silent','listen'))

