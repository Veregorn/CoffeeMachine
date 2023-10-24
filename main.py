# Data structures
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

# Global variables
user_input = ''
money = 0

# TODO: Create a function that prints the parameters of the coffee machine
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# TODO: Create a main loop so the machine can serve next customer when current operation has finished
while True:

    # TODO: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    user_input = input(" What would you like? (espresso/latte/cappuccino): ")

    # We need to have a condition for the App to exit
    if user_input == 'off':
        break
    elif user_input == 'report':
        print_report()

# TODO: Check resources sufficient
