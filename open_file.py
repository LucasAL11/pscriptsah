import logging
import tkinter.filedialog as filedialog


def open_file():
    """
    Abre uma janela de dialogo para selecionar um arquivo zip/rar,
    e retorna o caminho do arquivo selecionado.

    :return: O caminho do arquivo zip selecionado.
    :rtype: str
    """
    try:
        selected_file = filedialog.askopenfilename(
            filetypes=[("Zip Files", "*.zip"), ("Rar Files", "*.rar")]
        )
        return selected_file

    except Exception as e:
        raise ValueError(f"Erro ao abrir arquivo: {e}")