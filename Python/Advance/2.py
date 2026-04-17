class EvenNumberIterator:
    def __init__(self,stop):
        self.start = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            val = self.start
            self.start += 2
            return val
        else:
            raise StopIteration


obj = EvenNumberIterator(20)
for i in obj:
    print(i)