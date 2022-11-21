# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score1 = 0
score2 = 0
name = name1+name2

for char in name:
    if char == "T" or char == "R" or char == "U" or char == "t" or char == "r" or char == "u":
        score1 +=1
    if char == "L" or char == "O" or char == "V" or char == "l" or char == "o" or char == "v":
        score2 += 1
    if char == "E" or char == "e":
        score1 +=1
        score2 +=1

score = int(str(score1)+str(score2))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")