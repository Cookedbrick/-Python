#Как я понял, использовать .capitalize() и т.п. не нужно было?
def my_func(word):
    return (chr(ord(word[0])-32) + word[1:])
print(my_func('snow'))