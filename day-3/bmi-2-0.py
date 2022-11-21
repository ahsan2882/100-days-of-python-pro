# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)
bmi_int = round(bmi)

if bmi_int < 18.5:
    print(f"Your BMI is {bmi_int}, you are underweight.")
elif bmi_int < 25:
    print(f"Your BMI is {bmi_int}, you have a normal weight.")
elif bmi_int < 30:
    print(f"Your BMI is {bmi_int}, you are slightly overweight.")
elif bmi_int < 35:
    print(f"Your BMI is {bmi_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_int}, you are clinically obese.")