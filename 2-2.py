print('Вводите элементы списка или же "break" для остановки скрипта')
list_of_elements = []
element = 0
while 1:
    element = input()
    if element == 'break':
        break
    list_of_elements.append(element)
print(f'список до обмена {list_of_elements}')
for i in range(len(list_of_elements)//2):
    i *= 2
    list_of_elements[i], list_of_elements[i+1] = list_of_elements[i+1], list_of_elements[i]
print(f'список после обмена {list_of_elements}')