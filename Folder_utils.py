import os
import shutil

def create_local_folder(path):
    """
    Creates a local folder if it does not exist.

    Parameters
    ----------
    path : str
        The path to the folder to be created.

    Returns
    -------
    None
    """
    if not os.path.exists(path):
        os.makedirs(path)

def delete_local_folder(path):
    """
    Deletes a local folder if it exists.

    Parameters
    ----------
    path : str
        The path to the folder to be deleted.

    Returns
    -------
    None
    """
    if os.path.exists(path):
       shutil.rmtree(path, ignore_errors=True)

def verify_if_folder_is_server_path(path):
    """
    Verifies if a folder path is a server path.

    Parameters
    ----------
    path : str
        The path to the folder to be verified.

    Returns
    -------
    bool
        True if the path is a server path, False otherwise.

    """
    if path == r"\\plt-local.com.br\odin\Netuno\HinoAtualizador\ERP":
        return True
    else:
        return False
    
def get_current_path():
    """
    Gets the current working directory.

    Returns
    -------
    str
        The current working directory.
    """
    return os.getcwd()
