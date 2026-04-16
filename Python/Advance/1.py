"""
! Iterator:
    - It is an object which helps us to fetch the item one at a time from the collection or iterable.
    - It doest not store all the data in the memory.
    - Once it is completed, it can not be reused.

? Iterator :
    - Object -> Fetch one item at a time.

? Iterable :
    - On which we can loop over.

? Iteration :
    - This is a process of fetching item from the iterable.

! Iteration on inbuilt object :
    - Two functions are used for it :
        * iter() - return an iterator object
        * next() - To get the value from the iterable

! Iterating on user defined object :
    - 2 magic methods are used :
        * __iter__()
        * __next__()

"""

# ? Example of iteration on inbuilt object

l = [10,20,30,40]
iter_obj = iter(l)
print(next(iter_obj)) # 10
print(next(iter_obj)) # 20
print(next(iter_obj)) # 30
print(next(iter_obj)) # 40
# print(next(iter_obj))  
# ! This line will show StopIteration exception

# ? Example of iteration on user defined object

class myLoop():
    def __init__(self, start = 0, stop = 0 ,step = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop and self.step > 0 :
            self.start += self.step
            return self.start
        
        elif self.start > self.stop and self.step < 0:
            self.start += self.step
            return self.start
        else:
            raise StopIteration

obj = myLoop(10,0,-2)
for i in obj:
    print(i)


