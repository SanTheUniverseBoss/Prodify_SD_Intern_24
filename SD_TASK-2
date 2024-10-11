# GUESSING GAME

import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        try:
            # Ask for the user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is too low, too high, or correct
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess}.")
                print(f"It took you {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
