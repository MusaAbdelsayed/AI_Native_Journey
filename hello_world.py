def get_user_name():
    """Get the user's name and return it."""
    return input("Please enter your name: ")

def print_greeting(name):
    """Print a personalized greeting."""
    print(f"Hello, {name}! Welcome to the program!")

def main():
    """Main function to run the program."""
    # Get the user's name
    name = get_user_name()
    
    # Print the greeting
    print_greeting(name)

if __name__ == "__main__":
    main() 