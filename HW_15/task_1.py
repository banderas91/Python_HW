import os
from collections import namedtuple
import logging

logging.basicConfig(filename='directory_info.log', level=logging.INFO)

DirectoryInfo = namedtuple('DirectoryInfo', ['name', 'extension', 'is_directory', 'parent'])

def get_directory_info(directory_path):
    directory_info = []
    for root, dirs, files in os.walk(directory_path):
        for dir in dirs:
            info = DirectoryInfo(name=dir, extension=None, is_directory=True, parent=root)
            directory_info.append(info)
            logging.info(f'Directory: {info}')
        for file in files:
            name, extension = os.path.splitext(file)
            info = DirectoryInfo(name=name, extension=extension, is_directory=False, parent=root)
            directory_info.append(info)
            logging.info(f'File: {info}')
    return directory_info

if __name__ == '__main__':
    import sys
    directory_path = sys.argv[1]
    get_directory_info(directory_path)
