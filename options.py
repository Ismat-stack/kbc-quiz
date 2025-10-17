# options.py

def show_options():
    print("\n===== MAIN MENU =====")
    print("1. How to Play (Rules)")
    print("2. Play the Game")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1-3): "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 3.")
        return 0
