import json
with open('5-7.txt') as my_file:
    '''for i in my_file:
        print(re.findall('\d{2,}', i)[-1])'''
    my_dict = {i.split()[0]: int(i.split()[-2])-int(i.split()[-1])
              for i in my_file}
    json_list = [my_dict,{'average_profit': sum(i for i in my_dict.values() if i > 0)}]
    with open('json_5-7.json', 'w') as my_json:
        json.dump(json_list, my_json)
    
    
