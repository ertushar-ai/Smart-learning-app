from math_tutor import start_math_quiz
from calculator import run_calculator
from Trading_game_simulation import run_game


def main():
    while True:
        print("\n===== Smart Learning App =====")
        print("1. Math Tutor")
        print("2. Calculator")
        print("3. Trading Game")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_math_quiz()
            input("\nPress Enter to return to menu...")

        elif choice == '2':
            run_calculator()

        elif choice == '3':
            run_game()
            input("\nPress Enter to return to menu...")

        elif choice == '4':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()