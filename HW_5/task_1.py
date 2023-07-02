# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def get_file_info(file_path):
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1]
    file_path = os.path.dirname(file_path)
    return file_path, file_name, file_extension

result = get_file_info('/Users/antonkonycev/Documents/1ssh.ppk')
print(result)
