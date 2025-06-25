# -*- coding: utf-8 -*-
"""
Enhanced Simple Command-Line Calculator
A user-friendly calculator with basic arithmetic operations,
input validation, error handling, and calculation history.
"""

import sys
import os
from typing import Union, Tuple, List, Dict
from datetime import datetime

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
    print(f"{Colors.BOLD}{Colors.CYAN}🧮 Super Smart Calculator{Colors.END}")
    print(f"{Colors.BLUE}✨ Math made fun and easy!{Colors.END}")
    print(f"{Colors.HEADER}{'='*50}{Colors.END}\n")

def print_operations() -> None:
    """Display available operations with clear, fun instructions."""
    operations = [
        "➕ Add numbers together (+)",
        "➖ Subtract second number from first (-)", 
        "✖️  Multiply two numbers (*)",
        "➗ Divide first number by second (/)",
        "📊 Get remainder after division (%)",
        "💪 Raise first number to power of second (**)",
        "📋 Show your calculation history",
        "🔢 Exit calculator"
    ]
    
    print(f"{Colors.BOLD}{Colors.GREEN}🎯 What would you like to do?{Colors.END}")
    for i, op in enumerate(operations, 1):
        print(f"  {i}. {op}")
    print(f"{Colors.YELLOW}💡 Tip: Type 'h' anytime to see your history, or 'q' to quit!{Colors.END}\n")

def get_number(prompt: str) -> Union[float, None]:
    """Get and validate a number from user input with automatic comma removal."""
    while True:
        try:
            print(f"{Colors.CYAN}🔢 {prompt}{Colors.END}", end="")
            user_input = input().strip().lower()
            
            if user_input == 'q':
                return None
            
            # Remove commas from the input for better user experience
            user_input = user_input.replace(',', '')
                
            number = float(user_input)
            return number
            
        except ValueError:
            print(f"{Colors.RED}❌ Oops! That's not a valid number. Try again or type 'q' to quit.{Colors.END}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}👋 Calculator closed by user.{Colors.END}")
            sys.exit(0)

def get_operation() -> Union[str, None]:
    """Get and validate the operation choice from user."""
    while True:
        try:
            print(f"{Colors.CYAN}⚡ Pick your operation (1-8): {Colors.END}", end="")
            choice = input().strip().lower()
            
            if choice == 'q':
                return None
            elif choice == 'h':
                return 'history'
                
            operations = {
                '1': '+', '2': '-', '3': '*', 
                '4': '/', '5': '%', '6': '**'
            }
            
            if choice in operations:
                return operations[choice]
            else:
                print(f"{Colors.RED}❌ Please pick a number from 1-8, type 'h' for history, or 'q' to quit.{Colors.END}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}👋 Calculator closed by user.{Colors.END}")
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

def add_to_history(history: List[Dict], num1: float, operation: str, num2: float, result: Union[float, str], success: bool) -> None:
    """Add calculation to history list."""
    calculation_record = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'num1': num1,
        'operation': operation,
        'num2': num2,
        'result': result,
        'success': success
    }
    history.append(calculation_record)

def print_result(num1: float, num2: float, operation: str, success: bool, result: Union[float, str]) -> None:
    """Display the calculation result with formatting."""
    print(f"\n{Colors.HEADER}{'='*40}{Colors.END}")
    
    if success:
        print(f"{Colors.BOLD}{Colors.GREEN}🎉 Your Result:{Colors.END}")
        print(f"{Colors.CYAN}📊 {num1} {operation} {num2} = {result}{Colors.END}")
        print(f"{Colors.GREEN}✅ Calculation saved to history!{Colors.END}")
    else:
        print(f"{Colors.BOLD}{Colors.RED}❌ Calculation Error:{Colors.END}")
        print(f"{Colors.RED}🚫 {result}{Colors.END}")
    
    print(f"{Colors.HEADER}{'='*40}{Colors.END}\n")

def print_history(history: List[Dict]) -> None:
    """Display the calculation history."""
    if not history:
        print(f"{Colors.YELLOW}📝 No calculations in your history yet. Let's do some math!{Colors.END}\n")
        return
    
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}📋 YOUR CALCULATION HISTORY{Colors.END}")
    print(f"{Colors.HEADER}{'='*60}{Colors.END}")
    
    for i, calc in enumerate(history, 1):
        timestamp = calc['timestamp']
        num1 = calc['num1']
        operation = calc['operation']
        num2 = calc['num2']
        result = calc['result']
        success = calc['success']
        
        if success:
            print(f"{Colors.GREEN}✅ {i:2d}. [{timestamp}] {num1} {operation} {num2} = {result}{Colors.END}")
        else:
            print(f"{Colors.RED}❌ {i:2d}. [{timestamp}] {num1} {operation} {num2} = {result}{Colors.END}")
    
    print(f"{Colors.HEADER}{'='*60}{Colors.END}")
    print(f"{Colors.CYAN}📊 Total calculations: {len(history)}{Colors.END}\n")

def print_session_summary(history: List[Dict]) -> None:
    """Display session summary with statistics."""
    if not history:
        print(f"{Colors.YELLOW}📝 No calculations performed in this session.{Colors.END}")
        return
    
    successful_calcs = [calc for calc in history if calc['success']]
    failed_calcs = [calc for calc in history if not calc['success']]
    
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*50}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}📊 YOUR SESSION SUMMARY{Colors.END}")
    print(f"{Colors.HEADER}{'='*50}{Colors.END}")
    print(f"{Colors.CYAN}🔢 Total calculations: {len(history)}{Colors.END}")
    print(f"{Colors.GREEN}✅ Successful: {len(successful_calcs)}{Colors.END}")
    print(f"{Colors.RED}❌ Failed: {len(failed_calcs)}{Colors.END}")
    
    if successful_calcs:
        # Find most used operation
        operations = [calc['operation'] for calc in successful_calcs]
        most_used = max(set(operations), key=operations.count)
        print(f"{Colors.YELLOW}⭐ Your favorite operation: {most_used}{Colors.END}")
    
    print(f"{Colors.HEADER}{'='*50}{Colors.END}\n")

def print_features() -> None:
    """Display calculator features."""
    features = [
        "✅ Basic arithmetic operations (+, -, *, /, %, **)",
        "✅ Input validation and error handling",
        "✅ Division by zero protection",
        "✅ Clean, color-coded interface",
        "✅ Easy exit with 'q' command",
        "✅ Professional code structure",
        "✅ Type hints and documentation",
        "✅ Calculation history tracking",
        "✅ Session statistics and summary",
        "✅ Automatic comma removal for large numbers"
    ]
    
    print(f"{Colors.BOLD}{Colors.HEADER}Calculator Features:{Colors.END}")
    for feature in features:
        print(f"  {feature}")
    print()

def main() -> None:
    """Main calculator function with history tracking."""
    # Initialize calculation history
    calculation_history: List[Dict] = []
    
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
            elif operation == 'history':
                print_history(calculation_history)
                continue
                
            # Get second number
            num2 = get_number("Enter second number: ")
            if num2 is None:
                break
            
            # Perform calculation
            success, result = calculate(num1, num2, operation)
            print_result(num1, num2, operation, success, result)
            
            # Add to history
            add_to_history(calculation_history, num1, operation, num2, result, success)
            
            # Ask if user wants to continue
            print(f"{Colors.YELLOW}🔄 Press Enter to continue, 'h' for history, or 'q' to quit...{Colors.END}")
            user_choice = input().strip().lower()
            
            if user_choice == 'q':
                break
            elif user_choice == 'h':
                print_history(calculation_history)
                continue
                
            clear_screen()
            print_header()
        
        # Display session summary
        print_session_summary(calculation_history)
        print(f"\n{Colors.GREEN}🎉 Thanks for using the Enhanced Calculator! Come back soon!{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ An unexpected error occurred: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main() 