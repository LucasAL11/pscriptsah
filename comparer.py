import os
import logging
from validations import *
from Hasher_verifier import verify_hash_file

def compare_folders(path, remote_path, hversion):
    """
    Compara os arquivos de uma pasta local com os arquivos de uma pasta remota.

    Se o arquivo local existir na pasta remota, ele ser renomeado para ter o numero de versão como
    sufixo. Se o arquivo local nãoo existir na pasta remota, ele ser  copiado para a pasta remota.

    Parameters
    ----------
    path : str
        Caminho da pasta local que contem os arquivos a serem comparados.
    remote_path : str
        Caminho da pasta remota que ser comparada com a pasta local.
    hversion : str
        Numero de vers o utilizado como sufixo nos arquivos renomeados.

    Returns
    -------
    None
    """
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
                try:
                    os.rename(remote_path + '/' + file , remote_path + '/' + base_file + '.' + hversion)
                except Exception as e:
                    os.rename(remote_path + '/' + file , remote_path + '/' + base_file + '.' + hversion + '.bak')
                    os.rename(remote_path + '/' + file , remote_path + '/' + base_file + '.' + hversion + '.bak2')
                    os.rename(remote_path + '/' + file , remote_path + '/' + base_file + '.' + hversion + '.bak3')
                    logging.error(f"{e}")
                    os.remove(remote_path + '/' + base_file + '.' + hversion)
                
            os.rename(remote_path + '/' + file , remote_path + '/' + base_file + '.' + hversion)
        except Exception as e:
            logging.error(f"{e}")
