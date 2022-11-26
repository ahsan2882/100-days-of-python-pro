from art import logo
from replit import clear
# HINT: You can call clear() to clear the output in the console.
bidders = {}
isGameOver = False

print(logo)

while not isGameOver:
    name = input("What is your name?\n")
    bid = int(input("Enter your bid: $"))
    bidders[name] = bid
    play = input("Are there any more bidders (yes or no)\n")
    if play == "no":
        isGameOver = True
    else:
        clear()
clear()
max_bidder = ""
max_bid = 0
for bidder in bidders:
    if bidders[bidder] > max_bid:
        max_bid = bidders[bidder]
        max_bidder = bidder

print(f"The highest bidder is {max_bidder} with a bid of ${max_bid}")
