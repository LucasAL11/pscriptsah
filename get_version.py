import logging
from win32api import GetFileVersionInfo, HIWORD, LOWORD

def get_version_number(file_path):
    try:
        file_info = GetFileVersionInfo(file_path, "\\")
        ms_file_version = file_info['FileVersionMS']
        ls_file_version = file_info['FileVersionLS']
        version = f"{HIWORD(ms_file_version)}{LOWORD(ms_file_version)}{HIWORD(ls_file_version)}{LOWORD(ls_file_version)}"
        return version
    except Exception as e:
        if e.winerror == 1813 or e.winerror == 2:
            logging.error(f"Arquivo não encontrado ou inexistente: {file_path}")
            return 'no_version_found'
        else:
            raise e