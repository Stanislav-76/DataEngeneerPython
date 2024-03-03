# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами разных форматов.


import os
import json
import csv
import pickle


def write_json_csv_pickle(directory):
    # write_JSON
    result_dict_json = {}
    for dir_path, dir_file, file_name in os.walk(directory): 
        files = [f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
        dir = [f'DIRECTORY - {i} = {dir_size(dir_path + "/"+ i)} byte' for i in dir_file]
        dir.extend(files)
        result_dict_json[f'DIRECTORY - {dir_path}'] = dir
    with open('json_file.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict_json, json_file, indent=4, separators=(',', ':'))
    # write_CSV
    data = [["Dir", "Files"]]
    for key, value in result_dict_json.items():
        data.append([key, value])
    with open('csv_file.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)
    # write PICKLE
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(result_dict_json, pickle_file)


def dir_size(directory) -> int:
    for dir_path, dir_file, file_name in os.walk(directory):
        size = sum(os.path.getsize(dir_path + "/" + f) for f in os.listdir(os.path.abspath(dir_path)) if os.path.isfile(dir_path + "/" + f))
        if len(dir_file) == 0:
            return size
        else:
            return size + sum([dir_size(dir_path + "/" + f) for f in dir_file])
                        

write_json_csv_pickle(directory='Packet_HW8')
