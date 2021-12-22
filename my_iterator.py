import random

class my_iterator:
    def __init__(self, num):
        self.num = num
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.num:
            res = random.randint(1, 100)
            self.i += 1
            return res
        else:
            raise StopIteration

M = my_iterator(5)
for i in M:
   print (i)