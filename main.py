from Folder_utils import create_local_folder
from updater import *
from utils import get_current_path
from open_file import open_file
from zip_utils import extract_zip_file
import json

def main():
    local_path = get_current_path()

    with open('remote.config.json', 'r') as file:
        remote_paths = json.load(file)


    file = open_file()
    extract_zip_file(file, local_path)

    create_local_folder(local_path + '/att')

    for remote_path in remote_paths:
        update_remote_path(local_path + '/att', remote_path)

if __name__ == '__main__':
    main()