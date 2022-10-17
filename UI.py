# Menu
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Zukhra
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import add_delete
import search
import logger
import csv_mod


def menu():
    while True:
        z = input(
            "Введите 1, если хотите найти контакт. \nВведите 2, если хотите отредактировать существующий. \nВведите 3, если хотите добавить новый контакт. \nВведите 4, если хотите удалить контакт. \nДля выхода введите 0")
        
        match z:
            case '1':
                logger.number_logger("Выполняем поиск")
                search.search()
            case '2':
                logger.number_logger("Редактируем запись")
                csv_mod.write_file_csv(add_delete.add_note())
            case '3':
                 add_delete.add_note()
            case '4':
                return add_delete.delete_note()
            case '0':
                break



