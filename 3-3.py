def my_func(arg_1, arg_2, arg_3):
    sort_list  = [arg_1, arg_2, arg_3]
    sort_list.sort()
    return (sort_list[-1] + sort_list[-2])
print (my_func(4,2,6))
