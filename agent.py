import os
from datetime import datetime

from agent_core.model_router import route_task
from utils.logger import logger
from utils.excel_injector import inject_macro_to_excel
from utils.macro_executor import run_macro_and_check
from utils.file_manager import prompt_user_to_save_file, ensure_dir
from memory.memory_handler import remember_feedback

def save_output_to_file(macro_code):
    """Saves verified macro to a timestamped file in logs/macros/"""
    ensure_dir("logs/macros")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f"logs/macros/{timestamp}_macro.vba"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(macro_code)
    logger.info(f"✅ Macro saved successfully at: {filename}")
    return filename

def main():
    logger.info("🌸 RadhaRani MacroAgent starting up...")

    task_description = input("🔮 Describe your Excel macro task: ")

    # Step 1: Get initial macro from best-suited model
    macro_code, model_used = route_task(task_description)
    print(f"\n🌼 {model_used} says:\n{macro_code}")

    # Step 2: Ask for file to inject macro into
    target_path = prompt_user_to_save_file()
    inject_macro_to_excel(macro_code, target_path)

    # Step 3: Validate execution (retry if needed)
    success = run_macro_and_check(target_path, macro_code)
    if success:
        print("✅ Macro executed successfully on first try!")
        save_output_to_file(macro_code)
    else:
        print("❌ Macro failed initially. Retrying with fixes...")

        # Step 3.1: Allow user to give feedback/fix
        user_feedback = input("📝 Please provide the corrected version or error details:\n")
        if user_feedback.strip():
            remember_feedback(task_description, user_feedback, model_used)

            macro_code_retry, _ = route_task(task_description + " with corrections: " + user_feedback)
            inject_macro_to_excel(macro_code_retry, target_path)

            retry_success = run_macro_and_check(target_path, macro_code_retry)
            if retry_success:
                print("✅ Retry successful after applying correction!")
                save_output_to_file(macro_code_retry)
            else:
                print("💔 Retry also failed. Please try again with a refined instruction.")

if __name__ == "__main__":
    main()
