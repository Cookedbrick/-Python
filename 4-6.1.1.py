from sys import argv
from itertools import count

class MyIteratorCount():
    def __init__(self,arg_1):
       self.start_number = arg_1
       self.count = arg_1
    
    def __iter__(self):
        return self
    def __next__(self):
        
    end = start_number
    for i in count(start_number):
        if end == 0:
            break
        print(i)
        end -= 1