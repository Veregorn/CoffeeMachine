from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    

    while True:
        user_input = input(f" What would you like? ({menu.get_items()}): ")

        # We need to have a condition for the App to exit
        if user_input == 'off':
            break
        elif user_input == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            menu_item = menu.find_drink(user_input)
            if menu_item:
                if coffee_maker.is_resource_sufficient(menu_item):
                    if money_machine.make_payment(menu_item.cost):
                        coffee_maker.make_coffee(menu_item)

# si tu script es importado en otro programa, el código dentro del bloque if no se ejecutará automáticamente (habría que llamar a la función de forma explícita)
if __name__ == "__main__":
    main()