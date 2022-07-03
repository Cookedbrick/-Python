list_of_elements = [1, 2, 3, True, 'sdf', 'cswr', 1.234]
counter = 1
for i in list_of_elements:
    print(f'Элемент №{counter} имеет тип {type(i).__name__}')
    counter += 1