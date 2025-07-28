from core.router import choose_model_for_task
from core.memory import log_task_result
from core.feedback_handler import handle_feedback

def main():
    print("🌸 Welcome to Radha-Routed Reasoning Engine (R3E) 🌸")
    
    while True:
        task = input("\n🧘 Enter your task (or 'exit'): ")
        if task.lower() == 'exit':
            break
        
        task_type = "code"  # In future, detect this dynamically
        model_func = choose_model_for_task(task, task_type)
        
        if model_func:
            result = model_func(task)
            print(f"\n🌼 Model Output:\n{result}")
            
            feedback = input("🙏 Was this output satisfactory? (y/n): ").lower()
            if feedback == 'y':
                log_task_result(task, model_func.__name__, success=True)
            else:
                correction = input("📝 Please provide correction (if any): ")
                handle_feedback(task, correction, model_func.__name__)
                log_task_result(task, model_func.__name__, success=False)

if __name__ == "__main__":
    main()
