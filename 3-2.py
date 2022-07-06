def p_data(city, phone_number, email, year, name, surname):
    print(f'{name},{surname}, год рождения - {year} , город рождения - {city},\
 email - {email}, телефон - {phone_number}')
p_data(
       name = 'Фёдор',
       email = 'pepeo@mail.fr',
       year = '1984',
       surname = 'Добронравов',
       city = 'Находка',
       phone_number = '+912545689525'
       )
