a = int(input('Введите целое положительное число \n'))
greatest = 0
remainder = 0
while a != 0:
    remainder = a%10
    if remainder > greatest:
        greatest = remainder
    a //= 10
    
print(greatest)