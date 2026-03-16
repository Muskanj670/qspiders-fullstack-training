# Generator: It is a function where we have a sequance of operation by reaching each and every element present inside the collection. For generator we use a keyword yield.
# or
# A function that contains atleast one yield keyword knowns as generator function.
# To archieve generator we have to use type-casting.

# *****Difference between yield and return*****
# Return is a keyword which is ued to control the flow of execution by executing value.
# Yield is a keyword which is used to keep the sequence of the operation by terminating iteration and starting the same iteration without stopping the sequence.
# Return will work with any function. Type-casting is not required.
# Yield will work only with generator function. Type-casting is required.
# 

def gen():
    print("Hello")
    yield 
    print("Hii")
    yield 1
    print('Bye')
    yield [1,2]

print(list(gen()))