#!/usr/bin/env python3
"""
Interactive Hello World Script
This script demonstrates basic Python input/output, function organization,
and error handling with a personalized greeting system.
"""

def get_user_name() -> str:
    """
    Get the user's name and return it.
    
    Returns:
        str: The user's name, stripped of whitespace
    """
    while True:
        try:
            name = input("Please enter your name: ").strip()
            if not name:
                print("Error: Name cannot be empty. Please try again.")
                continue
            return name
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

def print_welcome(name: str) -> None:
    """
    Print a welcome message with the user's name.
    
    Args:
        name (str): The user's name
    """
    print(f"\nWelcome {name} to Python Programming!")
    print("This is a simple welcome message script.")
    print(f"Hello {name}, we're glad to have you here!")

def print_greeting(name: str) -> None:
    """
    Print a personalized greeting.
    
    Args:
        name (str): The user's name
    """
    print(f"Hello, {name}! Welcome to the program!")

def main() -> None:
    """Main function to run the program."""
    try:
        # Get the user's name
        name = get_user_name()
        
        # Print both welcome and greeting messages
        print_welcome(name)
        print("\n" + "="*50 + "\n")  # Add a separator
        print_greeting(name)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main() 