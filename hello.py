import os
import time

running = True

def math():
    user_input = input("Enter: ")
    result = eval(user_input)
    print("Result", result)
    print("Click Enter to continue...")
    if (input != "bye"):
        os.system('cls' if os.name == 'nt' else 'clear')

while running:
    math()
    print("\nType bye to leave")

    exit_choice = input("")
    if exit_choice == "bye":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Have a good day!")
        running = False
        time.sleep(1)
        
