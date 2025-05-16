MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

inserted_coins = {
    "quarter": 0,
    "dime": 0,
    "nickel": 0,
    "penny": 0,
}

profit = 0
drink = ""

def user_drink_check():
    """ensures the user's inputs for drinks are valid"""
    user = input("What would you like? (latte/ cappuccino/ espresso) ").lower()
    if user != 'latte' and user != 'cappuccino' and user != 'espresso' and user != 'report' and user != 'quit':
        print("That is not a valid choice")
        user = user_drink_check()
        return user
    else:
        return user

def user_coin_check(coin):
    """ensures the user's inputs for coins are valid"""
    try:
        if coin == "penny":
            user = int(input("How many pennies: "))
        else:
            user = int(input(f"How many {coin}s: "))
    except ValueError:
        print("That's not a valid number. Try again")
        user = user_coin_check(coin)
    return user

def calculate_user_payment():
    """calculates the amount that the user paid from the coins entered"""
    cash = 0
    for i in inserted_coins:
        cash += inserted_coins[i] * coins[i]
    return cash

def calculate_change(customer_payment):
    """returns the change based on what the customer ordered and paid"""
    change = round(customer_payment - MENU[drink]['cost'], 2)
    increase_profit()
    return change

def increase_profit():
    """modifies the overall profit that the coffee machine makes based on the drinks purchased"""
    global profit
    profit += MENU[drink]["cost"]

def reduce_resources():
    """reduces the remaining resources in the coffee machine based on the selected drink"""
    for i in MENU[drink]["ingredients"]:
        resources[i] -= MENU[drink]["ingredients"][i]
    
def print_resources():
    """prints the remaining resources in the coffee machine"""
    for i in resources:
        if i == "coffee":
            print(f"{i}: {resources[i]}g")
        else:
            print(f"{i}: {resources[i]}ml")            
    print(f"Money: ${profit:.2f}")

def print_menu():
    """prints the menu so the user knows the price of the drinks"""
    print("Here are the options and prices:")
    for i in MENU:
        print(f"{i.title()}: ${MENU[i]['cost']:.2f}")

def valid_resources():
    """checks that there are enough resources"""
    for i in MENU[drink]["ingredients"]:
        if resources[i] < MENU[drink]["ingredients"][i]:
            print(f"Not enough resources to make your {drink}")
            return False
    return True

def valid_pay(pay):
    """checks that the amount that the user input was enough to cover the amount that the drink they ordered costs"""
    if pay < MENU[drink]["cost"]:
        print("Not enough money")
        return False
    else:
        return True

def ask_coins():
    """prompts the character to enter in the amount of coins that the user wants to use"""
    for i in inserted_coins:
        inserted_coins[i] = user_coin_check(i)

def main():
    """main function that handles the operations necessary of the coffee machine"""
    global drink 
    drink = user_drink_check()
    if drink == "report":
        print_resources()
        main()
    elif drink == "quit":
        print("Thanks for ordering from the machine")
    else:
        ask_coins()
        user_pay = calculate_user_payment()
        if valid_pay(user_pay) == True and valid_resources() == True: # if the user's pay is enough to cover the drink and there are enough resources to make the drink, this runs
            reduce_resources()
            print(f"Your change is ${calculate_change(user_pay):.2f}")
            print(f"Here is your {drink}!")
        main()

print_menu()
main()

"""REMEMBER - You got this"""