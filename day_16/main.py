from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU_LIST = {
    "l": "latte",
    "e": "espresso",
    "c": "cappuccino"
}

maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

making_coffee = True
while making_coffee:

    choice = input("What would you like? (Espresso/Latte/Cappuccino \n").lower()

    if choice == 'r' or choice == "report":
        maker.report()
    elif choice in MENU_LIST:
        drink = menu.find_drink(MENU_LIST[choice])
        available = maker.is_resource_sufficient(drink)
        if available:
            payment_accepted = money.make_payment(drink.cost)
            if payment_accepted:
                maker.make_coffee(drink)
            else:
                making_coffee = False

        else:
            making_coffee = False
