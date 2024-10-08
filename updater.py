import os
import shutil
from Folder_utils import create_local_folder, verify_if_folder_is_server_path
from Hasher_verifier import verify_hash_file
from get_version import get_version_number
from comparer import compare_folders
import tqdm


total_files = 0


def update_remote_path_v2(local_path, remote_path):
    """
    This function updates a remote path with the files from a local path.

    If the remote path is a server path, it will be backed up to a "BKP" folder
    with the current version number before being updated.

    If the remote path is not a server path, it will be updated by comparing the
    files in the local path with the files in the remote path, and then copying
    the files that are newer or do not exist in the remote path.

    Parameters
    ----------
    local_path : str
        The path to the local folder containing the files to be updated.
    remote_path : str
        The path to the remote folder to be updated.

    Returns
    -------
    None
    """
    if local_path is None or remote_path is None:
        raise ValueError("local_path and remote_path must not be null")

    version = get_version_number(remote_path + "/Hino.wfa.exe")

    if verify_if_folder_is_server_path(remote_path):
        backup_path = remote_path.rsplit("\\", 1)[0]
        backup_folder = backup_path + "/" + "BKP" + "/" + version

        if not os.path.exists(backup_folder):
            shutil.copytree(remote_path, backup_folder)

        if not os.path.exists(remote_path):
            create_local_folder(remote_path)

        _update_files(local_path, remote_path)

    else:
        compare_folders(local_path, remote_path, version)
        _update_files(local_path, remote_path)


def update_remote_path(local_path, remote_path):
    """
    Atualiza a pasta remota com os arquivos da pasta local.

    Se a pasta remota for uma pasta de servidor, ela ser  backupada para uma pasta
    chamada "BKP" com o n mero de vers o atual.

    Se a pasta remota n o for uma pasta de servidor, os arquivos da pasta local ser o
    comparados com os arquivos da pasta remota e os arquivos que forem diferentes
    ser o atualizados na pasta remota.

    Parameters
    ----------
    local_path : str
        Caminho da pasta local que cont m os arquivos a serem atualizados.
    remote_path : str
        Caminho da pasta remota que ser  atualizada.

    Returns
    -------
    None
    """
    version = get_version_number(remote_path + "/Hino.wfa.exe")

    if verify_if_folder_is_server_path(remote_path):
        backup_path = remote_path.rsplit("\\", 1)[0]
        if not os.path.exists(backup_path + "/" + "BKP" + "/" + version):
            shutil.copytree(
                remote_path, backup_path + "/" + "BKP/" + version, dirs_exist_ok=True
            )

        if not os.path.exists(remote_path):
            create_local_folder(remote_path)

        for root, dirs, files in os.walk("./att"):
            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(remote_path, file)
                retrier_count = 0
                max_tries = 10

                hash = verify_hash_file(src_file, dst_file)
                if not hash:
                    while retrier_count < max_tries:
                        shutil.copy2(src_file, dst_file)
                        hash = verify_hash_file(src_file, dst_file)
                        if hash:

                            break
                        else:
                            retrier_count += 1
        return

    if os.path.isdir(remote_path):
        compare_folders(local_path, remote_path, version)

        total_files = sum(len(files) for _, _, files in os.walk("./att"))

    with tqdm.tqdm(total=total_files, desc="", unit="arquivos", leave=True) as pbar:
        for root, dirs, files in os.walk("./att"):
            for file in files:
                src_file = os.path.join(local_path, file)
                dst_file = os.path.join(remote_path, file)
                retrier_count = 0
                max_tries = 10

                pbar.set_description(f"Verificando arquivo: {file}")
                hash = verify_hash_file(src_file, dst_file)

                pbar.set_description(f"Copiando arquivo: {file}")

                while retrier_count < max_tries:
                    try:
                        shutil.copy2(src_file, dst_file)
                        pbar.set_description(f"Verificando arquivo: {file}")
                        hash = verify_hash_file(src_file, dst_file)

                        if hash:
                            pbar.set_postfix(text=f"Arquivo copiado: {file}")
                            break
                        else:
                            pbar.set_postfix(
                                text=f"Tentando copiar arquivo novamente: {file}"
                            )
                            retrier_count += 1
                    except Exception as e:
                        pbar.set_postfix(text=f"Erro ao copiar arquivo: {file}")
                        pbar.set_postfix(
                            text=f"tentando copiar arquivo novamente: {file}"
                        )
                        retrier_count += 1

                pbar.update(1)


def _update_files(local_path, remote_path):
    """
    Atualiza os arquivos na pasta remota com base nos arquivos presentes na pasta local.

    :param local_path: Caminho da pasta local.
    :param remote_path: Caminho da pasta remota.
    """
    total_files = sum(len(files) for _, _, files in os.walk("./att"))

    with tqdm.tqdm(total=total_files, desc="", unit="arquivos", leave=True) as pbar:
        for root, dirs, files in os.walk("./att"):
            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(remote_path, file)
                retrier_count = 0
                max_tries = 10

                pbar.set_description(f"Verificando arquivo: {file}")

                while retrier_count < max_tries:
                    shutil.copy2(src_file, dst_file)
                    pbar.set_description(f"Verificando arquivo: {file}")
                    hash = verify_hash_file(src_file, dst_file)

                    if not hash:
                        pbar.set_description(
                            text=f"Tentando copiar arquivo novamente: {file}"
                        )
                        retrier_count += 1
                        break

                    pbar.set_description(text=f"Arquivo copiado: {file}")

                pbar.update(1)
