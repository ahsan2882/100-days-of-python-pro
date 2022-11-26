#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? "))
num_of_people = int(input("How many people to split the bill? "))
#Format the result to 2 decimal places = 33.60
per_person = round((total_bill / num_of_people)*(1 + (tip_percent / 100)), 2)
print("Each person should pay: ${:.2f}".format(per_person))

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇