import os
import logging
import hashlib
from validations import *
from win32api import GetFileVersionInfo, HIWORD, LOWORD



def verify_hash_file(file_path, remote_file_path):
    hash1 = hashlib.new('sha256')
    hash2 = hashlib.new('sha256')
    try:
        with open(file_path, 'rb') as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                hash1.update(byte_block)
        with open(remote_file_path, 'rb') as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                hash2.update(byte_block)
        return hash1.hexdigest() == hash2.hexdigest()
    except Exception as e:
        logging.error(f"Error verifying hash: {e}")
        return False

def get_current_path():
    return os.getcwd()

def compare_folders(path, remote_path, hversion):
    ignore = [".", "..", ".DS_Store"]
    logging.info(f"Comparing folders {path} and {remote_path}")
    for file in os.listdir(path):
        logging.info(f"Checking file {file}")
        if file in os.listdir(remote_path):
            logging.info(f"File found: {file}")
            if file not in ignore:
                logging.warning(f"Duplicate file found: {file}")
                if not validate_if_file_exists(remote_path, file):
                    logging.debug(f"File does not exist in remote path: {file}")
                    continue
                if not (file.endswith('.dll') or file.endswith('.exe')):
                    logging.debug(f"File is not an executable or library: {file}")
                    continue
                base_file = file.replace('.dll', '').replace('.exe', '')
                logging.info(f"Verifying hash of files: {file}")
                if not verify_hash_file(path + '/' + file, remote_path + '/' + base_file + '.' + hversion):
                    logging.error(f"Hash mismatch: {file}")
                    continue
                if base_file + '.' + hversion in os.listdir(remote_path):
                    logging.debug(f"File already exists in remote path: {file}")
                    continue
                if not verify_hash_file(path + '/' + file, remote_path + '/' + base_file + '.' + hversion):
                    logging.error(f"Hash mismatch: {file}")
                    continue
                if file.endswith('.exe') and base_file + '.' + hversion not in os.listdir(remote_path):
                    logging.info(f"Renaming file: {file} to {base_file + '.' + hversion}")
                    os.rename(remote_path + '/' + file, remote_path + '/' + base_file + '.' + hversion)
                if not verify_hash_file(path + '/' + file, remote_path + '/' + base_file + '.' + hversion):
                    logging.error(f"Hash mismatch: {file}")
                    continue