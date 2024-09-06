import os
import logging
from validations import *
from Hasher_verifier import verify_hash_file

def compare_folders(path, remote_path, hversion):
    
    ignore = [".", "..", ".DS_Store"]
    logging.info(f"Comparando arquivos de {path} e {remote_path}")
    for file in os.listdir(path):
        try:
            logging.warning(f"Verificando se arquivo existe {file}")
            if file in os.listdir(remote_path):
                logging.warning(f"Arquivo encontrado: {file}")

            if file not in ignore:
                base_file = file.replace('.dll', '').replace('.exe', '').replace('.xml','')
                logging.warning(f"Renomeando arquivo: {file}")

            if os.path.isfile(remote_path + '/' + base_file + '.' + hversion):
                logging.warning(f"Arquivo ja existe: {base_file + '.' + hversion}")
                os.rename(remote_path + '/' + base_file + '.' + hversion , remote_path + '/' + base_file + '.' + hversion + '.bak')
                
            os.rename(remote_path + '/' + file, remote_path + '/' + base_file + '.' + hversion)
            logging.warning(f"renomeado arquivo: {base_file + '.' + hversion}")
        except Exception as e:
            logging.error(f"{e}")