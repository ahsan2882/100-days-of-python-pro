# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

time_left_yrs = 90-int(age)

months = time_left_yrs * 12
weeks = time_left_yrs * 52
days = time_left_yrs * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")