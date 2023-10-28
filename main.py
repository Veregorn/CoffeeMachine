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

COIN_VALUES = {'quarter': 0.25, 'dime': 0.10, 'nickle': 0.05, 'penny': 0.01}

def print_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(selected_coffee):
    """returns True if resources are sufficient to make the selected coffee.
    Otherwise, prints a message about the missing resource and returns False"""
    required_ingredients = MENU[selected_coffee]["ingredients"]

    for ingredient, amount in required_ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
        
    return True

def process_coins_to_dollars():
    total = 0
    
    print("Please insert coins.")
    
    for coin in COIN_VALUES.keys():
        num_coins = int(input(f"how many {coin}s?: "))
        total += COIN_VALUES[coin] * num_coins
    
    return total

def calc_change(product, dollars):
    return dollars - MENU[product]["cost"]

def make_coffee(type):
    for ingredient, amount in MENU[type]["ingredients"].items():
        resources[ingredient] -= amount

    print(f"Here is your {type} ☕️. Enjoy!")

def main():
    money = 0

    while True:
        user_input = input(" What would you like? (espresso/latte/cappuccino): ")

        # We need to have a condition for the App to exit
        if user_input == 'off':
            break
        elif user_input == 'report':
            print_report(money)
        elif user_input in MENU.keys():
            if not check_resources(user_input):
                continue
            else: # There is plenty of all resources needed
                dollars_inserted = process_coins_to_dollars()
                change = calc_change(user_input, dollars_inserted)
                if change < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else: # Enough money inserted
                    # Update machine's coins box
                    money += MENU[user_input]["cost"]
                    if change > 0: # Offer it to the costumer
                        print(f"Here is ${change} dollars in change.")
                    # Everything is fine: Let's make the coffee ☕️
                    make_coffee(user_input)
            
# si tu script es importado en otro programa, el código dentro del bloque if no se ejecutará automáticamente (habría que llamar a la función de forma explícita)
if __name__ == "__main__":
    main()