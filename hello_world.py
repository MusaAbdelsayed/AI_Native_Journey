# -*- coding: utf-8 -*-
"""
Interactive Hello World Script
This script demonstrates basic Python input/output, function organization,
and error handling with a personalized greeting system.
"""

def get_user_name() -> str:
    while True:
        try:
            name = input("Please enter your name: ").strip()
            if not name:
                print("Error: Name cannot be empty. Please try again.")
                continue
            return name.title()  # Capitalize each word
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

def print_welcome(name: str) -> None:
    if name == "Musa":
        print("\nHey, it's the awesome AI Director! Welcome back!")
        print("We're thrilled to have you here!")
    else:
        print(f"\nWelcome {name} to Python Programming!")
        print("This is a simple welcome message script.")
        print(f"Hello {name}, we're glad to have you here!")

def print_greeting(name: str) -> None:
    if name == "Musa":
        print("Hello, Awesome AI Director! Your presence makes this program special!")
    else:
        print(f"Hello, {name}! Welcome to the program!")

def main() -> None:
    try:
        name = get_user_name()
        print_welcome(name)
        print("\n" + "="*50 + "\n")
        print_greeting(name)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main() 