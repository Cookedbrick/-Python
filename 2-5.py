# Не свосем понимал, разрешено ли использовать .sort(reverse = True) в данном
# задании, поэтому cделел вот так.
print('Вводите числа для добавления в рейтинг или же "break"\
для остановки скрипта\n')
my_list = [7, 5, 3, 3, 2]

while 1:
    index = 0
    loop_variable = 0
    newbie = input(f'Текущий рейтинг {my_list}\n')
    if newbie == 'break':
        break
    newbie = int(newbie)
    for i in my_list:
        if newbie > i:
            my_list.insert(index, newbie)
            loop_variable = 1
            break
        index += 1
    if loop_variable == 1: continue
    my_list.append(newbie)
        
