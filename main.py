from Folder_utils import create_local_folder, delete_local_folder, get_current_path
from updater import *
from open_file import open_file
from zip_utils import extract_archive_file
import json


remote_paths = [
    r"\\10.0.100.220\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.221\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.222\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.226\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.227\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.228\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.229\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.230\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.235\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.238\C$\\Hino\\ERP\\wfa\\",
    r"\\10.0.100.240\C$\\Hino\\ERP\\wfa\\",
    r"\\plt-local.com.br\odin\Netuno\HinoAtualizador\ERP",
]


def main():

    file = open_file()
    local_path = get_current_path()
    create_local_folder(local_path + "/att")
    extract_archive_file(file, local_path) 
   
    for remote_path in remote_paths:
        print(R"iniciando atualização de: " + remote_path)
        update_remote_path(local_path + "/att", remote_path) 
    delete_local_folder(local_path + "/att")
if __name__ == "__main__":
    main()