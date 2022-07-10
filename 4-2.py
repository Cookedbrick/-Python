fist_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
sort_list = [ fist_list[i] for i in range(1, len(fist_list)) if fist_list[i] > fist_list[i-1]]
print (sort_list)
