from datetime import datetime

print("=" * 50)
print("🤖 Welcome to STUDY Assistant AI Chatbot")
print("Type 'help' to see available commands")
print("Type 'bye' to exit")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    # Greetings
    if user in ["hii","hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Name
    elif "name" in user:
        print("Bot: My name is GATE Assistant Bot.")

    # How are you
    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current Time =", current_time)

    # Date
    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date =", current_date)

    # GATE
    elif "gate" in user:
        print("Bot: GATE is a national-level examination for engineering graduates.")

    # Aptitude
    elif "aptitude" in user:
        print("Bot: General Aptitude carries 15 marks in GATE.")

    # Python
    elif "python" in user:
        print("Bot: Python is a high-level programming language widely used in AI and Data Science.")

    # C language
    elif "c language" in user or user == "c":
        print("Bot: C is a powerful programming language used for system programming.")

    # AI
    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    # Internship
    elif "internship" in user:
        print("Bot: Internships help students gain practical industry experience.")

    # Help Menu
    elif user == "help":
        print("\nAvailable Commands:")
        print("- hi")
        print("- hello")
        print("- how are you")
        print("- name")
        print("- time")
        print("- date")
        print("- gate")
        print("- aptitude")
        print("- python")
        print("- c language")
        print("- ai")
        print("- internship")
        print("- bye")

    # Exit
    elif user in ["bye", "exit", "quit","ok then"]:
        print("Bot: Thank you for using GATE Assistant Bot.")
        print("Bot: Goodbye! 👋")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that command.")
