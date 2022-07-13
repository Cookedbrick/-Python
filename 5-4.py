translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
    }
with open('5-4.txt') as f_in:
    with open('5-4_out.txt', 'w') as f_out:
        for i in f_in:
            f_out.write('{} {}\n'.format(
                translate[i.split()[0]], ' '.join(i.split()[1:])))

        