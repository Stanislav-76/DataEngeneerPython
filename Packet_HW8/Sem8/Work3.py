# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv
import os


def read_json():
    if os.path.exists('result1.json'):
        with open('result1.json', 'r', encoding='utf-8') as json_file:
            access_dict = json.load(json_file)
    else:
        access_dict = {"1": {},
                       "2": {},
                       "3": {},
                       "4": {},
                       "5": {},
                       "6": {},
                       "7": {}}
    return access_dict


def write_json(access_dict):
    while True:
        name = input("Введите имя: ")
        while True:
            flag = False
            ident = input("Введите ID: ")
            for keys, values in access_dict.items():
                if ident in values.keys():
                    print("Такой ID уже есть.")
                    flag = True
            if not flag:
                break
        while True:
            access_level = input("Веедите уровень доступа: ")
            if "0" < access_level < "8":
                break
        access_dict[access_level][ident] = name
        x = input("Выйти из цикла? y/n\n")
        if x == 'y':
            break
    with open('result1.json', 'w', encoding='utf-8') as json_file:
        json.dump(access_dict, json_file, indent=4, ensure_ascii=False)
    with open('result1.csv', 'w', encoding='utf-8') as csv_file:
        for key, value in access_dict.items():
            for key2, value2 in value.items():
                csv_file.write(f'{key},{key2},{value2}\n')
        # csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerows(access_dict)


if __name__ == "__main__":
    write_json(read_json())
