__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

path = r'C:/Users/lonni/OneDrive/Documents/Winc/files/cache'
if os.path.exists(path):
    shutil.rmtree(path)
else:
    os.mkdir(path)


def cache_zip(zip_file, cache_dir_path):
    with zipfile.ZipFile(zip_file, 'r') as zipref:
        zipref.extractall(cache_dir_path)
        return


cache_zip(r'C:/Users/lonni/OneDrive/Documents/Winc/files/data.zip', 'C:/Users/lonni/OneDrive/Documents/Winc/files/cache')


def cached_files():
    cache = os.path.abspath(r'C:/Users/lonni/OneDrive/Documents/Winc/files/cache')
    os.listdir(r'C:/Users/lonni/OneDrive/Documents/Winc/files/cache')
    return cache


def find_password(cache):
    directory = r'C:/Users/lonni/OneDrive/Documents/Winc/files/cache'
    for file in os.scandir(directory):
        password = str.find('password')
        if password in file:
            f = open(file, 'r')
            print('found password')
        else:
            print('password not found')
    return f, find_password
