__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

# declaring paths that will work on any computer
path = os.getcwd()
cache = os.path.join(path, 'files', 'cache')
data_zip = os.path.join(path, 'files', 'data.zip')


def clean_cache():
    """
    checks ik directory 'cache' exits, and removes it.
    Finally it creates an empty 'cache' directory
    """
    if not os.path.exists(cache):
        os.mkdir(cache)
    else:
        shutil.rmtree(cache)
        os.mkdir(cache)


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
        list.append(cache + file)
    return list


def find_password(cached_files):
    """
    From the list of files find the file(s) that containts 'password'
    Find the specific word 'password'
    Separate password from rest of file
    """
    password = 'password'
    for file in os.listdir(os.chdir(cache)):
        if file.endswith('.txt'):
            file_path = f'{file}'
            with open(file_path) as file:
                lines = file.readlines()
                for line in lines:
                    if password in line:
                        password = line.split(': ')
                        return password[1]


if __name__ == "__main__":
    clean_cache()
    cache_zip(data_zip, cache)
    cached_files()
    print(find_password(cached_files))
