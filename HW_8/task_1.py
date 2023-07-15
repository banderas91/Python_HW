# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
# Для тестированию возьмите pickle версию файла из предыдущей задачи. 
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv

def pickle_to_csv(pickle_file, csv_file):
    
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    with open(csv_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

pickle_to_csv('result.pickle', 'res.csv')

