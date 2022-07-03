list_of_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input('Введите номер месяца.\n'))
if 2 < month < 6:
    print(list_of_seasons[1])
elif 5 < month < 9:
    print(list_of_seasons[2])
elif 8 < month < 12:
    print(list_of_seasons[3])
else:
    print(list_of_seasons[0])


dict_of_seasons = {1:'Зима',
                   2:'Зима',
                   3:'Весна',
                   4:'Весна',
                   5:'Весна',
                   6:'Лето',
                   7:'Лето',
                   8:'Лето',
                   9:'Осень',
                   10:'Осень',
                   11:'Осень',
                   12:'Зима',}
print(dict_of_seasons.get(month))

dict_and_list = {'Зима': [1,2,12], 'Весна': [3,4,5], 'Лето': [6,7,8], 'Осень': [9,10,11]}
for items in dict_and_list.items():
    if month in items[1]: print (items[0])