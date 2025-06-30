# A simple Python script for GitHub demonstration
import datetime

def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}! Welcome to GitHub."

def get_current_time():
    """Returns the current date and time as a formatted string."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def main():
    name = input("Enter your name: ")
    message = greet(name)
    print(message)
    print(f"Current time: {get_current_time()}")

if __name__ == "__main__":
    main()
