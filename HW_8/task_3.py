import os
import json
import csv
import pickle

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def walk_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            result.append({
                'name': name,
                'path': dir_path,
                'parent': root,
                'type': 'directory',
                'size': get_size(dir_path)
            })
        for name in files:
            file_path = os.path.join(root, name)
            result.append({
                'name': name,
                'path': file_path,
                'parent': root,
                'type': 'file',
                'size': os.path.getsize(file_path)
            })
    return result

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def save_to_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

directory = '/Users/antonkonycev/Library/Containers/Mail.Ru.DiskO.as/Data/Disk-O.as.mounts/banderas91@mail.ru-mailru/Geek/HW_Python/python_HW'
data = walk_directory(directory)
save_to_json(data, 'result.json')
save_to_csv(data, 'result.csv')
save_to_pickle(data, 'result.pickle')
