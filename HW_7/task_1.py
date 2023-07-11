'''1 — Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>'''

import os

def rename_files(new_name, txt, json):
    i = 1
    for filename in os.listdir():
        if filename.endswith(txt):
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_{new_name}_{i}.{json}"
            os.rename(filename, new_filename)
            i += 1
rename_files('new_name', 'txt', 'json')