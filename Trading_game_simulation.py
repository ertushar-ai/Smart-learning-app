import random

def run_game():
    marbles_in_bag = (
        "green", "green", "green", "green", "green",
        "black", "red", "red", "red", "white",
    )

    starting_money = int(input("Enter your starting money: "))
    current_money = starting_money
    rounds = int(input("Enter no. of rounds to play: "))

    marble = "none"

    print(f"\nYou start with {starting_money} coins.")

    for r in range(1, rounds + 1):
        print(f"\nRound {r} | Current coins: {current_money} | Last draw: {marble}")

        bet = int(input("How much do you want to bet? "))

        if bet > current_money:
            print("You can't bet more than you have!")
            continue

        marble = random.choice(marbles_in_bag)

        if marble == "green":
            result = bet
            print("You WON!")
        elif marble == "red":
            result = -bet
            print("You LOST!")
        elif marble == "black":
            result = bet * 10
            print("JACKPOT!!! 🎉")
        elif marble == "white":
            result = -bet * 5
            print("BIG LOSS 💀")

        current_money += result

        print(f"Result: {marble} ({result}) | Balance: {current_money}")

        if current_money <= starting_money / 2:
            print("\nGame over! You lost too much money.")
            break

    print("\nStarting | Ending coins:", starting_money, "/", current_money)
    print("Gain/Loss %:", round(((current_money - starting_money) / starting_money) * 100, 2))