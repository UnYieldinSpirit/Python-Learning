# Tip Calculator
# What was the total bill
# How much tip, 10, 12 or 15%?
# How many people to split the bill?
# Final result: Each person should pay: output number
print("Welcome to the tip calculator!")
initial_bill = float(input("What was the total bill?'\n"))
initial_bill = round(initial_bill, 2)

tip_percentage = float(input("How much tip: 10, 12, or 15%?\n"))
tip_percentage /= 100 # converts the entered "percentage" into a decimal number capable of arithmetic operations

number_of_people = int(input("How many people are splitting the bill?\n"))

tip = initial_bill * tip_percentage # stores the total tip amount

total = initial_bill + tip # calculates the total bill that needs to be split

split_bill = total / number_of_people # splits the bill
split_bill = round(split_bill, 2)

print(f"Each person should be paying: ${split_bill}")