import logging
import zipfile
import patoolib

def extract_archive_file(path_to_archive_file, directory_to_extract_to):
    """
    Extracts an archive file to a directory.

    Parameters
    ----------
    path_to_archive_file : str
        The path to the archive file to be extracted.
    directory_to_extract_to : str
        The directory to which the archive file should be extracted.

    Returns
    -------
    None
    """
    if path_to_archive_file.endswith(".zip"):
        with zipfile.ZipFile(path_to_archive_file, "r") as zip_ref:
            zip_ref.extractall(directory_to_extract_to + "/att")
    elif path_to_archive_file.endswith(".rar"):
        try:
            patoolib.extract_archive(
                path_to_archive_file, outdir=directory_to_extract_to + "/att"
            )
        except patoolib.util.PatoolError as e:
            logging.error(f"Erro ao extrair arquivo: {e}")
    else:
        raise ValueError(f"Unsupported archive type: {path_to_archive_file}")