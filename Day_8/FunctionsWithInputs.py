def greet():
    print("Hello")
    print("How do you do?")
    print("Howdy")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today, {name}?")
    print(f"Ain't the weather mighty fine, {name}?")

username = input("What is your name? ")
greet_with_name(username)

def life_in_weeks(week_life):
    print(f"You have {week_life} left.")
    
age = int(input("How old are you? "))

weeks_left = (90 - age) * 52

life_in_weeks(weeks_left)