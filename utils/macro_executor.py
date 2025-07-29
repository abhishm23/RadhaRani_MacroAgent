import time
import win32com.client as win32
from utils.logger import logger

def run_macro(workbook_path, macro_name):
    try:
        logger.info(f"🧪 Running macro '{macro_name}' in {workbook_path}")
        excel = win32.Dispatch("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False

        wb = excel.Workbooks.Open(workbook_path)

        # Run the macro
        excel.Application.Run(f"'{wb.Name}'!{macro_name}")
        logger.info("✅ Macro executed successfully.")

        wb.Close(SaveChanges=True)
        excel.Quit()
        return True, None

    except Exception as e:
        logger.error(f"❌ Error while running macro: {str(e)}")
        return False, str(e)
