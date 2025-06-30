# A simple Python script for GitHub demonstration

def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}! Welcome to GitHub."

def main():
    name = input("Enter your name: ")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()
