__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

# declaring paths that will work on any computer
path = os.getcwd()
cache = os.path.join(path, 'cache')
data_zip = os.path.join(path, 'data.zip')


def clean_cache():
    """
    checks ik directory 'cache' exits, and removes it.
    Finally it creates an empty 'cache' directory
    """
    if os.path.exists(cache):
        shutil.rmtree(cache)
    else:
        os.mkdir(os.path.join(cache))


def cache_zip(zip_file, cache_dir_path):
    """
    unpacks the zip file into specified directory
    """
    with zipfile.ZipFile(zip_file, 'r') as zipref:
        zipref.extractall(cache_dir_path)


def cached_files():
    """
    This function creates a list of all files in the 'cache' directory
    """
    list = []
    for file in os.listdir(cache):
        list = os.path.join(file, cache)
        list.append(list.file)
    return list


def find_password(cache):
    """
    From the list of files find the file(s) that containts 'password'
    Find the specific word 'password'
    Separate password from rest of file and print it
    """
    directory = cache
    for file in os.scandir(directory):
        password = str.find('password')
        if password in file.name:
            f = open(file.path, 'r')
        else:
            pass
    return f


if __name__ == "main":
    clean_cache()
    cache_zip()
    cached_files()
    find_password()
