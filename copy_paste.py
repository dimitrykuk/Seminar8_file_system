from return_data_file import data_file
from print_data import print_file

def copy():
    data1, nf1 = data_file()
    count_rows = len(data1)
    if count_rows == 0:
        print("Файл пустой!"
              "Копировать нечего!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}, которую нужно скопировать: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}, которую нужно скопировать: "))
        copy_row = data1[number_row-1].split(";")
        print("Выберите файл, в который нужно вставить")
        data2, nf2 = data_file()
        with open(f'db/data_{nf2}.txt', 'a', encoding='utf-8') as file:
            file.write(f'{len(data2)+1};{copy_row[2]};{copy_row[3]};{copy_row[4]}')
        print("Строка скопирована!")