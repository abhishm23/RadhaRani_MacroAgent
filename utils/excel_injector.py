import os
import win32com.client as win32
from utils.logger import logger

def inject_macro_to_excel(vba_code: str, workbook_path: str):
    """
    Injects a VBA macro into an Excel workbook (creates if not present).
    Determines correct FileFormat based on file extension.
    """
    logger.info("🔧 Injecting macro into workbook...")

    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False

    file_ext = os.path.splitext(workbook_path)[1].lower()

    file_format_map = {
        '.xlsm': 52,  # Macro-Enabled Workbook
        '.xlsb': 50,  # Binary Workbook
        '.xlsx': 51,  # Regular Workbook
        '.xls': 56,   # Legacy Excel 97-2003
    }

    file_format = file_format_map.get(file_ext)
    if file_format is None:
        raise ValueError(f"Unsupported file extension: {file_ext}")

    # Open or create workbook
    if os.path.exists(workbook_path):
        wb = excel.Workbooks.Open(workbook_path)
    else:
        wb = excel.Workbooks.Add()
        wb.SaveAs(Filename=workbook_path, FileFormat=file_format)

    try:
        vb_module = wb.VBProject.VBComponents.Add(1)  # 1 = Standard Module
        vb_module.CodeModule.AddFromString(vba_code)

        wb.Save()
        wb.Close()
        logger.info(f"✅ Macro injected and workbook saved: {workbook_path}")
        print(f"\n✨ Macro injected into: {workbook_path}")
    except Exception as e:
        logger.error(f"❌ Error injecting macro: {e}")
        print(f"\n❌ Failed to inject macro: {e}")
    finally:
        excel.Quit()
