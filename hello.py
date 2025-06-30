# A simple Python script for GitHub demonstration
import datetime

def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}! Welcome to GitHub."

def get_current_time():
    """Returns the current date and time as a formatted string."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def calculate(a, b, operation):
    """A simple calculator function.
    
    Args:
        a (float): First number
        b (float): Second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'
        
    Returns:
        float: Result of the calculation
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")

def main():
    name = input("Enter your name: ")
    message = greet(name)
    print(message)
    print(f"Current time: {get_current_time()}")
    
    # Simple calculator demo
    print("\nCalculator Demo:")
    print(f"5 + 3 = {calculate(5, 3, 'add')}")
    print(f"5 - 3 = {calculate(5, 3, 'subtract')}")
    print(f"5 * 3 = {calculate(5, 3, 'multiply')}")
    print(f"5 / 3 = {calculate(5, 3, 'divide'):.2f}")

if __name__ == "__main__":
    main()
