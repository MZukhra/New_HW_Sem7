# Добавление поиска
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Victoria Burakhina
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import add_read_write

def search():
    surname = input('Введите фамилию: ')
    d = add_read_write.read_csv()
    if surname in d.keys():
        print(f'{surname} {"".join(d[surname])}')
    else:
        print('Данных нет в списке')
        print('Выход в общее меню')
