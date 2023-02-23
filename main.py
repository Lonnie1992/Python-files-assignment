__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

def clean_cache():
    path = os.getcwd()
    cache = os.path.join(path, r'files/cache')
    for file_name in os.listdir(cache):
        file = cache + file_name
        if os.path.isfile(file):
            os.remove(file)
            shutil.rmtree(os.path.join(path, r'files/cache'))
        else:
            os.mkdir(os.path.join(path, r'files/cache'))
            return clean_cache


def cache_zip(zip_file, cache_dir_path):
    with zipfile.ZipFile(zip_file, 'r') as zipref:
        zipref.extractall(cache_dir_path)
        return cache_zip


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
