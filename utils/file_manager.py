import os
from tkinter import filedialog, Tk

def prompt_user_to_save_file(default_name="RadhaRani_MacroWorkbook.xlsm"):
    """
    Opens a save file dialog for the user to choose the destination Excel file.
    """
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.asksaveasfilename(
        title="📁 Select where to save the macro-injected workbook",
        defaultextension=".xlsm",
        filetypes=[("Excel Macro-Enabled Workbook", "*.xlsm")],
        initialfile=default_name
    )
    root.destroy()
    return file_path

def ensure_dir(directory_path):
    """
    Ensures that the specified directory exists. If not, creates it.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)