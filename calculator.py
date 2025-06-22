# -*- coding: utf-8 -*-
"""
Simple Command-Line Calculator
A user-friendly calculator with basic arithmetic operations,
input validation, and error handling.
"""

import sys
import os
from typing import Union, Tuple

class Colors:
    """ANSI color codes for enhanced output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen() -> None:
    """Clear the terminal screen for better presentation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header() -> None:
    """Display the calculator header."""
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*50}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}Simple Command-Line Calculator{Colors.END}")
    print(f"{Colors.BLUE}Basic Arithmetic Operations{Colors.END}")
    print(f"{Colors.HEADER}{'='*50}{Colors.END}\n")

def print_operations() -> None:
    """Display available operations."""
    operations = [
        "➕ Addition (+)",
        "➖ Subtraction (-)", 
        "✖️  Multiplication (*)",
        "➗ Division (/)",
        "📊 Modulo (%)",
        "💪 Power (**)",
        "🔢 Exit (q)"
    ]
    
    print(f"{Colors.BOLD}{Colors.GREEN}Available Operations:{Colors.END}")
    for i, op in enumerate(operations, 1):
        print(f"  {i}. {op}")
    print()

def get_number(prompt: str) -> Union[float, None]:
    """Get and validate a number from user input."""
    while True:
        try:
            print(f"{Colors.CYAN}{prompt}{Colors.END}", end="")
            user_input = input().strip().lower()
            
            if user_input == 'q':
                return None
                
            number = float(user_input)
            return number
            
        except ValueError:
            print(f"{Colors.RED}Error: Please enter a valid number or 'q' to quit.{Colors.END}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Calculator terminated by user.{Colors.END}")
            sys.exit(0)

def get_operation() -> Union[str, None]:
    """Get and validate the operation choice from user."""
    while True:
        try:
            print(f"{Colors.CYAN}Choose operation (1-7): {Colors.END}", end="")
            choice = input().strip().lower()
            
            if choice == 'q':
                return None
                
            operations = {
                '1': '+', '2': '-', '3': '*', 
                '4': '/', '5': '%', '6': '**'
            }
            
            if choice in operations:
                return operations[choice]
            else:
                print(f"{Colors.RED}Error: Please enter a number between 1-7 or 'q' to quit.{Colors.END}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Calculator terminated by user.{Colors.END}")
            sys.exit(0)

def calculate(num1: float, num2: float, operation: str) -> Tuple[bool, Union[float, str]]:
    """Perform the calculation and return result with success status."""
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return False, "Error: Division by zero is not allowed!"
            result = num1 / num2
        elif operation == '%':
            if num2 == 0:
                return False, "Error: Modulo by zero is not allowed!"
            result = num1 % num2
        elif operation == '**':
            result = num1 ** num2
        else:
            return False, f"Error: Unknown operation '{operation}'"
            
        return True, result
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def print_result(num1: float, num2: float, operation: str, success: bool, result: Union[float, str]) -> None:
    """Display the calculation result with formatting."""
    print(f"\n{Colors.HEADER}{'='*40}{Colors.END}")
    
    if success:
        print(f"{Colors.BOLD}{Colors.GREEN}Calculation Result:{Colors.END}")
        print(f"{Colors.CYAN}{num1} {operation} {num2} = {result}{Colors.END}")
    else:
        print(f"{Colors.BOLD}{Colors.RED}Calculation Error:{Colors.END}")
        print(f"{Colors.RED}{result}{Colors.END}")
    
    print(f"{Colors.HEADER}{'='*40}{Colors.END}\n")

def print_features() -> None:
    """Display calculator features."""
    features = [
        "✅ Basic arithmetic operations (+, -, *, /, %, **)",
        "✅ Input validation and error handling",
        "✅ Division by zero protection",
        "✅ Clean, color-coded interface",
        "✅ Easy exit with 'q' command",
        "✅ Professional code structure",
        "✅ Type hints and documentation"
    ]
    
    print(f"{Colors.BOLD}{Colors.HEADER}Calculator Features:{Colors.END}")
    for feature in features:
        print(f"  {feature}")
    print()

def main() -> None:
    """Main calculator function."""
    try:
        clear_screen()
        print_header()
        print_features()
        
        while True:
            print_operations()
            
            # Get first number
            num1 = get_number("Enter first number: ")
            if num1 is None:
                break
                
            # Get operation
            operation = get_operation()
            if operation is None:
                break
                
            # Get second number
            num2 = get_number("Enter second number: ")
            if num2 is None:
                break
            
            # Perform calculation
            success, result = calculate(num1, num2, operation)
            print_result(num1, num2, operation, success, result)
            
            # Ask if user wants to continue
            print(f"{Colors.YELLOW}Press Enter to continue or 'q' to quit...{Colors.END}")
            if input().strip().lower() == 'q':
                break
                
            clear_screen()
            print_header()
        
        print(f"\n{Colors.GREEN}Thank you for using the Simple Calculator!{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}An unexpected error occurred: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main() 