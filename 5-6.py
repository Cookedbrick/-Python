import re
my_dir = {}
with open('5-6.txt') as my_file:
    for i in my_file:
        my_dir[re.search('[а-яА-ЯёЁ]{4,}', i).group()] = sum(int(i) for i in re.findall('(\d+)', i))
    