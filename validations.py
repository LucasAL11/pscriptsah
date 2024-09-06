import os

def Verify_if_remote_path_exists(path):
    if(os.path.isdir(path)):
        return True
    else:
        return False
