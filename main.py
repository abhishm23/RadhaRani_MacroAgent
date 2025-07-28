# main.py
import os
from agent.core import AIEngine

def main():
    print("🌸 Radha Rani's Devoted AI Agent 🌸")
    print("Type 'exit' to stop.\n")

    engine = AIEngine()

    while True:
        user_input = input("👤 You: ")
        if user_input.strip().lower() == "exit":
            print("🙏 Jai Radhe Radhe! Exiting gracefully.")
            break

        response = engine.get_response(user_input)
        print(f"🤖 Agent: {response}")

if __name__ == "__main__":
    main()
