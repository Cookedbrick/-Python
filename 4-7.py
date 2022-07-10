from math import factorial

def fact(num):
    for i in range(1,num+1):
        yield factorial(i)
for i,j in enumerate(fact(5), 1):
    print(f'{i}!',j)