MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
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

profit = 0

def user_choice():
    """ensures that the user inputs are valid"""
    user = input("What would you like? (latte/ cappuccino/ espresso) ").lower()
    if user != 'latte' and user != 'cappuccino' and user != 'espresso' and user != 'report':
        print("That is not a valid choice")
        user = user_choice()
        return user
    else:
        return user
    
def calculate_change(customer_payment, drink):
    change = customer_payment - MENU[drink]['cost']
    return change

