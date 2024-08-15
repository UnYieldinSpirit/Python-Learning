print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches?\n"))
bill = 0

if height >= 48:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55: # logical operator checking more than one condition
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("You can not ride this coaster bucko.")