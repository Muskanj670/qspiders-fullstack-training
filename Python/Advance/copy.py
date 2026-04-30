"""
* In python we 3 types of copy:
    1. General Copy :
         - Indicates to same reference (Change in one's value will reflect in others too)
    2. Shallow Copy :
         - Indicates to new reference
         -  Can be done by using two ways
             -> Slicing
             -> copy()
    3. Deep Copy
"""

# ! General Copy

def general_copy():
    l1 = [10,20,30]
    l2 = l1
    print(f"{id(l1)} = {l1}")
    print(f"{id(l2)} = {l2}")

    l2[0] = 100

    print(f"{id(l1)} = {l1}")
    print(f"{id(l2)} = {l2}")

# general_copy()


# ! Shallow copyright

import copy as c

def shallow():
    l1 = [10,20,30]
    l2 = l1[::]
    print(f"{id(l1)} = {l1}")
    print(f"{id(l2)} = {l2}")

    l2[0] = 100

    print(f"{id(l1)} = {l1}")
    print(f"{id(l2)} = {l2}")

shallow()
