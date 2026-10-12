import os
import time


running = True


def math():
    user_input = input("Eneter calculation: ")
    result = eval(user_input)
    print("result:", result)
    print("Click Enter to continue")
    if (input != "bye"):
        os.system('cls' if os.name == 'nt' else 'clear')


while running:
    math()
    print("\nType bye to exit or click ENter to continue")

    exit_i = input("")
    if exit_i == "bye":
        print("Exiting")
        running = False
        time.sleep(1)
