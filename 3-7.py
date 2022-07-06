def three_seven(text):
    def my_func(word):
        return (chr(ord(word[0])-32) + word[1:])
    string = []
    for i in text.split():
        string.append(my_func(i))
    string = ' '.join(string)
    return (string)
print(three_seven('text for test'))
