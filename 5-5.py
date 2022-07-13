from random import randint

with open('5-5.txt', 'w+') as my_file:
    my_file.write(' '.join(str(randint(-10,10))  for i in range(randint(1,20))))
    my_file.seek(0)
    print(sum(int(i) for i in my_file.read().split()))
    
    
    
    
