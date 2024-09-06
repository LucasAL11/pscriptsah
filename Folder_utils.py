import os

def create_local_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def delete_local_folder(path):
    if os.path.exists(path):
        os.rmdir(path)

def verify_if_folder_is_server_path(path):
    if path == r"\\plt-local.com.br\odin\Netuno\HinoAtualizador\ERP":
        return True
    else:
        return False