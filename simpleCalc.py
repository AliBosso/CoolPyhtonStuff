import time
import os

running = True

def math():
    operation = input("Operation: ")
    val1 = input("Value 1: ")
    if(operation == "sqrt"):
        result = float(val1) ** 0.5
    else:
        val2 = input("Value 2: ")

        if (operation == "+"):
            result = float(val1) + float(val2)
        elif (operation == "-"):
            result = float(val1) - float(val2)
        elif (operation == "*"):
            result = float(val1) * float(val2)
        elif (operation == "/"):
            result = float(val1) / float(val2)
        elif(operation == "pow"):
            result = float(val1) ** float(val2)
        elif(operation == "%"):
            result = float(val1) % float(val2)
    print("Result:", result)
    print("\nPress Enter to continue...")
    if input() == "":
        os.system('cls' if os.name == 'nt' else 'clear')
        math()  


def hardMath():
    user_input = input("Enter your math desires: ")
    result = eval(user_input)
    print("Rsult ", result)
    print("\nPress Enter to continue...")
    if input() == "":
        os.system('cls' if os.name == 'nt' else 'clear')
        hardMath()  



while running:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 1. Ask the question ONLY ONCE and save it to a variable
    choice = input("Simple math? y/n ").strip().lower()

    # 2. Check the variable instead of calling input() again
    if choice == "y":
        math()
        print("\nType 'exit', 'bye', or 'quit' to exit the program.")
        
        # FIXING THE EXIT CHECKS (explained below)
        exit_choice = input("")
        if exit_choice in ["exit", "bye", "quit"]:
            running = False
            print("Exiting...")
            time.sleep(1)

    elif choice == "n":
        hardMath()
        print("\nType 'exit', 'bye', or 'quit' to exit the program.")
        
        # FIXING THE EXIT CHECKS
        exit_choice = input("")
        if exit_choice in ["exit", "bye", "quit"]:
            running = False
            print("Exiting...")
            time.sleep(1)
