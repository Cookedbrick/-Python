def three_seven():
    def my_func(word):
        return (chr(ord(word[0])-32) + word[1:])
    string = []
    for i in input('Введите предложение\n').split():
        string.append(my_func(i))
    string = ' '.join(string)
    return (string)
print(three_seven())
