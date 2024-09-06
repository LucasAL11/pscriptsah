import tkinter.filedialog as filedialog

def open_file():
    """
    Abre uma janela de dialogo para selecionar um arquivo zip,
    e retorna o caminho do arquivo selecionado.

    :return: O caminho do arquivo zip selecionado.
    :rtype: str
    """
    selected_file = filedialog.askopenfilename(filetypes=[('Zip Files', '*.zip')])
    return selected_file