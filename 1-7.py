a = float(input('Введите дальность пробежки в перый день\n'))
b = float(input('Введите желаемую дальность пробежки\n'))
day = 1
while a <= b:
    a *= 1.1
    day += 1
print (day)