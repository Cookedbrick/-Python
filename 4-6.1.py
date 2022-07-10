from sys import argv
from itertools import count

start_number = int(argv[1])
end = start_number
for i in count(start_number):
    if end == 0:
        break
    print(i)
    end -= 1