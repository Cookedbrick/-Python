product_list = []
counter = 1
while 1:
    name = input('Введите наиманование товара\n')
    price = input('Введите цену товара\n')
    quantity = input('Введите количесво товара\n')
    unit = input('Введите еденицу измерения товара\n')
    product_list.append((counter, 
    {'Название': name, 'Цена': price, 'Колличество': quantity, 'Ед.': unit}))
    counter += 1
    if input('для продолжения ввода введите "+"') != '+':
        break
product_dict = {}
for i in product_list[0][1].keys():
    product_dict[i] = []
for i in product_dict.keys():
    for j in product_list:
        product_dict[i].append(j[1].get(i))
for key, value in product_dict.items():
  print("{0}: {1}".format(key,value))
        