from service.openai_service import OpenAIService

def main():
    while True:
        display_menu()
        choice = get_user_choice()
        execute_choice(choice)

def display_menu():
    print("Welcome to the OpenAI API Explorer")
    print("1. Text Completion")
    print("2. Image Generation")
    print("3. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-3): ")
    return choice

def execute_choice(choice):
    if choice == '1':
        #prompt = input("Enter your text to the AI: ")
        OpenAIService().simple_chat()
    elif choice == '2':
        prompt = input("Enter your image generation phrase to the AI: ")
        OpenAIService().generate_image(prompt)
    elif choice == '3':
        print("Exiting application. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
