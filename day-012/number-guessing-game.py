from art import logo
import random

# Number Guessing Game Objectives:

# Include an ASCII art logo.
print(logo)



def play_game():
    num_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        # Allow the player to submit a guess for a number between 1 and 100.
        guess = int(input("Make a guess: "))
        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
        # If they got the answer correct, show the actual answer to the player.
        if guess == num_to_guess:
            print(f"You got it! The answer was {num_to_guess}.")
            return
        elif guess > num_to_guess:
            print("Too high.")
        else:
            print("Too low.")
        # Track the number of turns remaining.
        attempts -= 1
    # If they run out of turns, provide feedback to the player.
    print("You have run out of guesses, you lose.")
    print(f"The number was {num_to_guess}.")


play_game()





