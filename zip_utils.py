import zipfile

def extract_zip_file(path_to_zip_file, directory_to_extract_to):
    """
    Extracts a zip file to a directory.

    Parameters
    ----------
    path_to_zip_file : str
        The path to the zip file to be extracted.
    directory_to_extract_to : str
        The directory to which the zip file should be extracted.

    Returns
    -------
    None
    """
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to + '/att')