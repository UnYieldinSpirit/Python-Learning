from sys import version
print(version)

# Create a BMI calculator when the user enters in their weight (lbs) and height (inches)
weight = float(input("Please enter your current weight (in lbs):\n"))
height = float(input("Please enter your current height (in inches):\n"))

# BMI calcutions
bmi = (weight / (height ** 2)) * 703 # 703 is the factor that must be multiplied by when using the imperial system.

user_diagnosis = " " # holds the user's final diagnosis

#if else statements to discover the users' status (under or overweight)
if bmi <= 18.5:
    user_diagnosis = "underweight"
elif bmi > 18.5 and bmi < 24.9:
    user_diagnosis = "normal weight"
elif bmi > 25 and bmi < 29.9:
    user_diagnosis = "overweight"
else:
    user_diagnosis = "obese"

print(f"Your BMI is as follows: {bmi} \n This means that you are: {user_diagnosis}")