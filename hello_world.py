# -*- coding: utf-8 -*-
"""
Enhanced Interactive Hello World Script
This script demonstrates advanced Python features including:
- Input validation and error handling
- Conditional logic and personalization
- Color output and formatting
- Multiple special user recognition
- Timestamp and session tracking
"""

import datetime
import sys
import os

# ANSI color codes for enhanced output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def get_user_name() -> str:
    """Get and validate user input with enhanced error handling."""
    while True:
        try:
            print(f"{Colors.CYAN}Please enter your name: {Colors.END}", end="")
            name = input().strip()
            if not name:
                print(f"{Colors.RED}Error: Name cannot be empty. Please try again.{Colors.END}")
                continue
            return name.title()  # Capitalize each word
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Program terminated by user.{Colors.END}")
            exit(0)
        except Exception as e:
            print(f"{Colors.RED}An error occurred: {e}{Colors.END}")
            print(f"{Colors.YELLOW}Please try again.{Colors.END}")

def get_special_message(name: str) -> tuple[str, str]:
    """Return special welcome and greeting messages based on user identity."""
    special_users = {
        "Musa": {
            "welcome": f"{Colors.BOLD}{Colors.GREEN}Hey, it's the awesome AI Director! Welcome back!{Colors.END}",
            "greeting": f"{Colors.BOLD}{Colors.GREEN}Hello, Awesome AI Director! Your presence makes this program special!{Colors.END}"
        },
        "John": {
            "welcome": f"{Colors.BOLD}{Colors.BLUE}Welcome back, John! Great to see you again!{Colors.END}",
            "greeting": f"{Colors.BOLD}{Colors.BLUE}Hello, John! You're a valued member of our community!{Colors.END}"
        },
        "Sarah": {
            "welcome": f"{Colors.BOLD}{Colors.YELLOW}Sarah! The coding wizard is back!{Colors.END}",
            "greeting": f"{Colors.BOLD}{Colors.YELLOW}Hello, Sarah! Your expertise lights up our program!{Colors.END}"
        }
    }
    
    return special_users.get(name, {
        "welcome": f"{Colors.CYAN}Welcome {name} to Python Programming!{Colors.END}\nThis is an enhanced welcome message script.\n{Colors.GREEN}Hello {name}, we're glad to have you here!{Colors.END}",
        "greeting": f"{Colors.GREEN}Hello, {name}! Welcome to the program!{Colors.END}"
    })

def print_welcome(name: str) -> None:
    """Display personalized welcome message with enhanced formatting."""
    special_messages = get_special_message(name)
    print(f"\n{special_messages['welcome']}")

def print_greeting(name: str) -> None:
    """Display personalized greeting message."""
    special_messages = get_special_message(name)
    print(f"{special_messages['greeting']}")

def print_session_info() -> None:
    """Display session information including timestamp and Python version."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    python_version = sys.version.split()[0]
    
    print(f"\n{Colors.HEADER}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}Session Information:{Colors.END}")
    print(f"{Colors.CYAN}Timestamp: {current_time}{Colors.END}")
    print(f"{Colors.CYAN}Python Version: {python_version}{Colors.END}")
    print(f"{Colors.CYAN}Script: Enhanced Hello World with Personalization{Colors.END}")
    print(f"{Colors.HEADER}{'='*60}{Colors.END}")

def print_features() -> None:
    """Display script features for demonstration purposes."""
    features = [
        "✅ Input validation and error handling",
        "✅ Conditional logic and personalization", 
        "✅ Color-coded output for better UX",
        "✅ Multiple special user recognition",
        "✅ Timestamp and session tracking",
        "✅ Professional code structure",
        "✅ Type hints and documentation"
    ]
    
    print(f"\n{Colors.BOLD}{Colors.HEADER}Script Features:{Colors.END}")
    for feature in features:
        print(f"  {feature}")

def main() -> None:
    """Main function orchestrating the enhanced greeting experience."""
    try:
        # Clear screen for better presentation
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{Colors.BOLD}{Colors.HEADER}Enhanced Interactive Hello World{Colors.END}")
        print(f"{Colors.CYAN}Welcome to the AI Native Journey Demo{Colors.END}\n")
        
        name = get_user_name()
        print_welcome(name)
        print_session_info()
        print_greeting(name)
        print_features()
        
        print(f"\n{Colors.GREEN}Thank you for using our enhanced greeting system!{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}An unexpected error occurred: {e}{Colors.END}")
        exit(1)

if __name__ == "__main__":
    main() 