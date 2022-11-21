# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissor. \n"))
your_choice = choices[choice]

computer = random.randint(0,2)
print(computer)
computer_choice = choices[computer]



print(f"You chose {your_choice}")
print(f"Computer chose {computer_choice}")

if choice == computer:
  print("Game draw")
elif choice == 0:
  if computer == 1:
    print("Computer wins")
  else:
    print("You win")
elif choice == 1:
  if computer == 0:
    print("You win")
  else:
    print("Computer wins")
else:
  if computer == 0:
    print("Computer wins")
  else:
    print("you win")