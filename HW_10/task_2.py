import os

class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_info(self):
        file_name = os.path.basename(self.file_path)
        file_extension = os.path.splitext(file_name)[1]
        file_path = os.path.dirname(self.file_path)
        return file_path, file_name, file_extension

file_info = FileInfo('/Users/antonkonycev/Documents/1ssh.ppk')
result = file_info.get_file_info()
print(result)
