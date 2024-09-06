import tkinter.filedialog as filedialog

def open_file():
    selected_file = filedialog.askopenfilename(filetypes=[('Zip Files', '*.zip')])
    return selected_file