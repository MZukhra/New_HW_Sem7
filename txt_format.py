

import logger

# первичная запись справочника
def write_txt(): #переделать под txt
    with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['first_name', 'contact info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'иванов', 'contact info': ['иван', '+79003001212', 'электрик']})
        writer.writerow({'first_name': 'сидоров', 'contact info': ['михаил', '+79621201588', 'сантехник']})
        writer.writerow({'first_name': 'карасев', 'contact info': ['карп', '+79198763232', 'нелюбит рыбалку']})

def write_txt_cols():
    phone_numbers = write_txt()
    with open('note.txt', 'w', encoding='utf-8', newline='') as file:
       for key in phone_numbers.keys():
        file.write(f'{key},\n{phone_numbers[key][0]}\n{phone_numbers[key][1]}\n{phone_numbers[key][2]}\n\n')
    logger.number_logger(f"Запись в столбик.")

def read_txt_col():
    with open('note.txt', 'r', encoding='utf-8', newline='') as file:
        readfile = file.read()
        tablo = ("".join(readfile))
        print(tablo)

  