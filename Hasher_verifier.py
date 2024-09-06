import hashlib
import logging

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
        #logging.error(f"erro ao verificar hash: {e}")
        return False
