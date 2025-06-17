def get_user_name():
    """Get the user's name and return it."""
    return input("Please enter your name: ")

def print_welcome(name):
    """Print a welcome message with the user's name."""
    print(f"Welcome {name} to Python Programming!")
    print("This is a simple welcome message script.")
    print(f"Hello {name}, we're glad to have you here!")

def print_greeting(name):
    """Print a personalized greeting."""
    print(f"Hello, {name}! Welcome to the program!")

def main():
    """Main function to run the program."""
    # Get the user's name
    name = get_user_name()
    
    # Print both welcome and greeting messages
    print_welcome(name)
    print("\n" + "="*50 + "\n")  # Add a separator
    print_greeting(name)

if __name__ == "__main__":
    main() 