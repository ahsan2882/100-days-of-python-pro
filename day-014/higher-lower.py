from game_data import data
from art import logo, vs
from random import choices
import os
def clear(): 
    return os.system('cls')


isGameOver = False
score = 0

while not isGameOver:
    print(logo)
    choiceA = choices(data)[0]
    choiceB = choices(data)[0]
    if choiceA["name"] != choiceB["name"]:
        if choiceA['follower_count'] > choiceB['follower_count']:
            correct = "A"
        else:
            correct = "B"
        print(
            f"Compare A: {choiceA['name']}, {choiceA['description']}, from {choiceA['country']}")
        print(vs)
        print(
            f"Compare B: {choiceB['name']}, {choiceB['description']}, from {choiceB['country']}")
        guess = input("Who has more followers, type 'A' or 'B': ")
        if guess.lower() == correct.lower():
            score += 1
            clear()
        else:
            isGameOver = True
            print(f"You got a score of {score}")
