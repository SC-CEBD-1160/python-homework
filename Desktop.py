#------------ Reach 2
import os

path = '/Users/sebastienchurch/Desktop/'
files = os.listdir(path)

for file in files:
    is_file = os.path.isfile(f'{path}{file}')
    is_dir = os.path.isdir(f'{path}{file}')
    if is_file:
        print(f'The name: {file} is a file')
    if is_dir:
        print(f'The name: {file} is a directory')