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
